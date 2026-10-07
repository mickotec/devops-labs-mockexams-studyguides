#!/usr/bin/env python3
"""
Exam Service for killer.sh / Linux Foundation Mock Exam Simulator.
Parses mock exams from curriculum.labs_mocks, extracts structured questions,
and interfaces with the lab runner for setup, grading, and reset.
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = TOOLS_DIR.parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Domain definitions and weights according to official Linux Foundation specs
CKA_DOMAINS = {
    "Storage": 10.0,
    "Troubleshooting": 30.0,
    "Workloads & Scheduling": 15.0,
    "Cluster Architecture, Installation & Configuration": 25.0,
    "Services & Networking": 20.0
}

LFCS_DOMAINS = {
    "Operations Deployment": 25.0,
    "Networking": 25.0,
    "Storage": 20.0,
    "Essential Commands": 20.0,
    "Users and Groups": 10.0
}

def load_mock_labs():
    """Loads raw mock labs from curriculum.labs_mocks."""
    from curriculum.labs_mocks import MOCK_LABS
    return {lab["lab_id"]: lab for lab in MOCK_LABS}


def get_question_context(track, exam_id, q_num, q_text, domain):
    """
    Returns realistic question-specific context command and target host.
    Follows real Linux Foundation and killer.sh examination conventions.
    """
    text_lower = q_text.lower()
    domain_lower = domain.lower()

    if track == "CKA":
        if "ssh node01" in text_lower or ("static pod" in text_lower and "node01" in text_lower):
            return "ssh node01", "node01"
        elif "ssh node02" in text_lower or ("node02" in text_lower and ("kubelet" in text_lower or "diagnose" in text_lower or "stopped" in text_lower)):
            return "ssh node02", "node02"
        elif "etcdctl" in text_lower or "snapshot" in text_lower or "kube-scheduler" in text_lower or "kubeadm" in text_lower or "controlplane" in text_lower:
            return "ssh controlplane", "controlplane"
        else:
            return "kubectl config use-context k8s", "controlplane"
    else:
        # LFCS Track
        if any(d in domain_lower for d in ["storage", "networking", "operations", "users"]):
            return "sudo -i", "lfcs"
        elif any(kw in text_lower for kw in ["lvm", "fstab", "systemctl", "iptables", "route", "useradd", "group", "swap", "mount"]):
            return "sudo -i", "lfcs"
        else:
            return "ssh student@172.16.16.16", "lfcs"


def parse_exam_questions(lab_dict):
    """
    Parses tasks and solution strings into structured question objects with
    domain, weight, context commands, text, and solution snippets.
    """
    exam_id = lab_dict.get("lab_id", "")
    track = lab_dict.get("track", "CKA")
    tasks_text = lab_dict.get("tasks", "")
    solution_text = lab_dict.get("solution", "")

    # Parse questions from tasks_text
    # Patterns: #### Domain: <Domain Name> (<Weight> ...)
    # Followed by: - **Q<Num>:** <Task text>
    
    questions = []
    current_domain = "General"
    current_weight = "5.0%"

    domain_blocks = re.split(r'####\s+Domain:\s*', tasks_text)
    
    # Check if there are domain blocks
    if len(domain_blocks) > 1:
        for block in domain_blocks[1:]:
            lines = block.strip().split('\n')
            header = lines[0]
            m_dom = re.match(r'([^(\n]+?)(?:\s*\(([^)]+)\))?$', header)
            if m_dom:
                current_domain = m_dom.group(1).strip()
                meta_info = m_dom.group(2) or ""
                m_weight = re.search(r'([\d\.]+)%\s*each', meta_info)
                if m_weight:
                    current_weight = f"{m_weight.group(1)}%"
                else:
                    current_weight = "5.0%"

            # Find all Q items in this block
            q_matches = list(re.finditer(r'-\s+\*\*Q(\d+):\*\*\s*(.+?)(?=\n-\s+\*\*Q\d+:|\Z)', block, re.DOTALL))
            for qm in q_matches:
                q_num = int(qm.group(1))
                q_text = qm.group(2).strip()
                context_cmd, target_host = get_question_context(track, exam_id, q_num, q_text, current_domain)

                questions.append({
                    "id": f"Q{q_num}",
                    "number": q_num,
                    "domain": current_domain,
                    "weight": current_weight,
                    "context_cmd": context_cmd,
                    "target_host": target_host,
                    "text": q_text,
                    "solution": ""
                })
    else:
        # Fallback regex for standard lists
        q_matches = list(re.finditer(r'-\s+\*\*Q(\d+):\*\*\s*(.+?)(?=\n-\s+\*\*Q\d+:|\Z)', tasks_text, re.DOTALL))
        for qm in q_matches:
            q_num = int(qm.group(1))
            q_text = qm.group(2).strip()
            context_cmd, target_host = get_question_context(track, exam_id, q_num, q_text, "Core Exam Tasks")
            questions.append({
                "id": f"Q{q_num}",
                "number": q_num,
                "domain": "Core Exam Tasks",
                "weight": "5.0%",
                "context_cmd": context_cmd,
                "target_host": target_host,
                "text": q_text,
                "solution": ""
            })

    # Sort questions by number
    questions.sort(key=lambda q: q["number"])

    # Extract solution snippets per question from solution_text
    sol_matches = list(re.finditer(r'####\s+Q(\d+):[^\n]*\n(.+?)(?=\n####\s+Q\d+:|\Z)', solution_text, re.DOTALL))
    sol_map = {int(sm.group(1)): sm.group(2).strip() for sm in sol_matches}
    for q in questions:
        if q["number"] in sol_map:
            q["solution"] = sol_map[q["number"]]

    return questions

def get_exam_metadata(exam_id):
    """Returns structured exam metadata ready for the killer.sh UI."""
    labs = load_mock_labs()
    if exam_id not in labs:
        return None

    lab = labs[exam_id]
    track = lab.get("track", "CKA")
    questions = parse_exam_questions(lab)
    domains = CKA_DOMAINS if track == "CKA" else LFCS_DOMAINS
    pass_score = "66%" if track == "CKA" else "67%"

    return {
        "exam_id": exam_id,
        "track": track,
        "title": lab.get("title", f"{track} Mock Exam"),
        "time_limit": lab.get("time", "120m"),
        "time_seconds": 120 * 60,
        "passing_score": pass_score,
        "domain_weights": domains,
        "total_questions": len(questions),
        "questions": questions,
        "tasks_raw": lab.get("tasks", ""),
        "solution_raw": lab.get("solution", "")
    }

def get_all_mock_exams():
    """Returns summary cards of all 4 mock exams."""
    labs = load_mock_labs()
    result = []
    order = ["mock-cka-1", "mock-cka-2"]
    for eid in order:
        if eid in labs:
            lab = labs[eid]
            track = lab.get("track", "CKA")
            result.append({
                "exam_id": eid,
                "track": track,
                "title": lab.get("title"),
                "time_limit": lab.get("time", "120m"),
                "passing_score": "66%" if track == "CKA" else "67%",
                "difficulty": "Hard (Exam Simulation)",
                "target": "VirtualBox K8s Cluster (controlplane, node01, node02)" if track == "CKA" else "VirtualBox Ubuntu VM (LFCS)"
            })
    return result

def run_exam_action(exam_id, action):
    """Executes start, check/grade, or reset for the specified mock exam."""
    valid_actions = {
        "start": f"./lab start {exam_id}",
        "grade": f"./lab check {exam_id}",
        "reset": f"./lab reset {exam_id}"
    }
    if action not in valid_actions:
        return False, f"Invalid action: {action}"

    cmd = valid_actions[action]
    res = subprocess.run(cmd, shell=True, cwd=str(BASE_DIR), capture_output=True, text=True)
    return (res.returncode == 0 or action == "grade"), res.stdout + ("\n" + res.stderr if res.stderr else "")

def parse_grade_output(exam_id, grade_text):
    """Parses output from ./lab check into structured score report."""
    labs = load_mock_labs()
    lab = labs.get(exam_id, {})
    track = lab.get("track", "CKA")

    # Strip ANSI escape codes for reliable regex parsing
    clean_text = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', grade_text)

    # Extract overall percentage
    # Pattern: Final Weighted Score: 6.0% or **6.0%**
    m_pct = re.search(r'Final Weighted Score:\s*(?:[^\d]*)([\d\.]+)%', clean_text)
    total_pct = float(m_pct.group(1)) if m_pct else 0.0

    # Extract questions passed
    m_qp = re.search(r'Questions Passed:\s*(\d+)\s*/\s*(\d+)', clean_text)
    passed_q = int(m_qp.group(1)) if m_qp else 0
    total_q = int(m_qp.group(2)) if m_qp else (17 if track == "CKA" else 20)

    # Extract pass/fail
    threshold = 66.0 if track == "CKA" else 67.0
    passed = total_pct >= threshold

    # Extract individual question statuses
    # Lines like: [PASS] Q1: ... or [FAIL] Q1: ...
    # Also load questions metadata to merge question text & solution
    questions = parse_exam_questions(lab)
    q_map = {q["id"]: q for q in questions}

    q_results = []
    for line in clean_text.splitlines():
        m_res = re.search(r'\[(PASS|FAIL)\]\s*(Q\d+):\s*(.+)', line)
        if m_res:
            status = m_res.group(1)
            qid = m_res.group(2)
            desc = m_res.group(3).strip()
            q_info = q_map.get(qid, {})
            q_results.append({
                "id": qid,
                "number": q_info.get("number", int(qid.replace("Q", "") if qid.startswith("Q") else 0)),
                "status": status,
                "detail": desc,
                "domain": q_info.get("domain", "Core"),
                "weight": q_info.get("weight", "5.0%"),
                "text": q_info.get("text", ""),
                "solution": q_info.get("solution", ""),
                "context_cmd": q_info.get("context_cmd", "")
            })

    # Sort results by question number
    q_results.sort(key=lambda r: r["number"])

    # Extract domain breakdowns
    domain_scores = []
    # Pattern: • Domain Name (X%):   X/Y passed   (Z% / W%)
    d_matches = re.finditer(r'•\s+([^(\n]+?)\s*\(([\d\.]+)%\):\s*(\d+)/(\d+)\s+passed\s+\(([\d\.]+)%\s*/\s*([\d\.]+)%\)', clean_text)
    for dm in d_matches:
        domain_scores.append({
            "domain": dm.group(1).strip(),
            "target_pct": float(dm.group(2)),
            "passed_count": int(dm.group(3)),
            "total_count": int(dm.group(4)),
            "score_pct": float(dm.group(5)),
            "max_pct": float(dm.group(6))
        })

    return {
        "exam_id": exam_id,
        "track": track,
        "title": lab.get("title", f"{track} Mock Exam"),
        "time_limit": lab.get("time", "120m"),
        "total_pct": total_pct,
        "threshold": threshold,
        "passed": passed,
        "passed_questions": passed_q,
        "total_questions": total_q,
        "domain_scores": domain_scores,
        "question_results": q_results,
        "raw_output": grade_text
    }


def format_duration(seconds):
    """Formats seconds into human-readable duration, e.g. '1h 24m 15s' or '45m 30s'."""
    if seconds is None or seconds < 0:
        return "0m 0s"
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"


RESULTS_DIR = Path.home() / ".local" / "share" / "study_todo"
RESULTS_FILE = RESULTS_DIR / "exam_results.json"
_MEMORY_RESULTS = {}


def save_exam_result(exam_id, report):
    """Persists exam result in memory and on disk."""
    _MEMORY_RESULTS[exam_id] = report
    try:
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        data = {}
        if RESULTS_FILE.exists():
            try:
                data = json.loads(RESULTS_FILE.read_text())
            except Exception:
                data = {}
        data[exam_id] = report
        RESULTS_FILE.write_text(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Warning: Failed to save exam results: {e}")


def get_exam_result(exam_id):
    """Retrieves saved exam result for the given exam_id."""
    if exam_id in _MEMORY_RESULTS:
        return _MEMORY_RESULTS[exam_id]
    if RESULTS_FILE.exists():
        try:
            data = json.loads(RESULTS_FILE.read_text())
            if exam_id in data:
                _MEMORY_RESULTS[exam_id] = data[exam_id]
                return data[exam_id]
        except Exception:
            pass
    return None


def submit_and_grade_exam(exam_id, time_spent_seconds=0):
    """
    Terminates the exam session, runs the full grading verification,
    formats duration and domain scorecards, enriches questions with solutions,
    saves the result report, and returns it.
    """
    ok, grade_text = run_exam_action(exam_id, "grade")
    report = parse_grade_output(exam_id, grade_text)

    try:
        time_spent_seconds = int(time_spent_seconds or 0)
    except (ValueError, TypeError):
        time_spent_seconds = 0

    report["time_spent_seconds"] = time_spent_seconds
    report["time_spent_formatted"] = format_duration(time_spent_seconds)
    report["submitted_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_exam_result(exam_id, report)
    return report

