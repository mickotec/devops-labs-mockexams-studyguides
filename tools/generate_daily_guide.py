#!/usr/bin/env python3
"""
CKA & LFCS Master Daily Study Guide Generator (Track-Separated)
Generates separate, publication-grade daily study guides for CKA and LFCS:
- CKA Daily Study Guides -> cka/guides/CKA_Daily_Study_Guide_W{w}D{d}_{date}.html
- LFCS Daily Study Guides -> lfcs/guides/LFCS_Daily_Study_Guide_W{w}D{d}_{date}.html

Features:
- Track-specific agendas (CKA Morning 08:00-12:00, LFCS Afternoon 15:00-18:00)
- Deep architectural & theoretical explanations
- High-resolution colorful vector SVG diagrams
- Hands-on lab candidate tasks and official grader walkthroughs
- Daily exam speed drills, shortcuts, and track-specific self-assessment checklists
- Headless Chromium compilation to publication-grade A4 PDF (when browser available)
- Multi-threaded parallel batch generation for all 48 days
"""

import os
import sys
import re
import html
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

# Resolve base paths
TOOLS_DIR = Path(__file__).resolve().parent
BASE_DIR = TOOLS_DIR.parent if TOOLS_DIR.name == "tools" else TOOLS_DIR
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Import curriculum package
from curriculum import get_curriculum

CKA_DIR = BASE_DIR / "cka"
LFCS_DIR = BASE_DIR / "lfcs"
CKA_GUIDES_DIR = CKA_DIR / "guides"
LFCS_GUIDES_DIR = LFCS_DIR / "guides"
CKA_GUIDES_DIR.mkdir(parents=True, exist_ok=True)
LFCS_GUIDES_DIR.mkdir(parents=True, exist_ok=True)

ICS_PATH = BASE_DIR / "cka_lfcs_schedule.ics"
if not ICS_PATH.exists():
    ICS_PATH = TOOLS_DIR / "cka_lfcs_schedule.ics"

START_DATE = datetime.strptime("20260914", "%Y%m%d")


def parse_ics_schedule(ics_file: Path):
    """Parse VCALENDAR events into a date-keyed dictionary."""
    if not ics_file or not ics_file.exists():
        return {}

    content = ics_file.read_text(encoding="utf-8")
    raw_events = content.split("BEGIN:VEVENT")
    schedule = {}

    for ev in raw_events[1:]:
        dt_m = re.search(r"DTSTART:([0-9]{8})", ev)
        sum_m = re.search(r"SUMMARY:(.*)", ev)
        desc_m = re.search(r"DESCRIPTION:(.*?)(?=\n[A-Z-]+:|\nEND:VEVENT)", ev, re.DOTALL)

        if dt_m and sum_m:
            d = dt_m.group(1)
            summary = sum_m.group(1).strip()
            desc = desc_m.group(1).replace(r"\n", "\n").strip() if desc_m else ""

            if d not in schedule:
                schedule[d] = {"date_str": d, "events": {}}

            if "[CKA]" in summary:
                schedule[d]["events"]["cka"] = {"summary": summary, "desc": desc}
            elif "[LFCS]" in summary:
                schedule[d]["events"]["lfcs"] = {"summary": summary, "desc": desc}
            elif "[RECOVERY]" in summary:
                schedule[d]["events"]["recovery"] = {"summary": summary, "desc": desc}

    return schedule


def extract_schedule_items(desc: str):
    """Extract individual timetable items from event description."""
    lines = desc.split("\n")
    items = []
    for line in lines:
        line = line.strip()
        if re.match(r"^[0-9]{2}:[0-9]{2}\s+(?:AM|PM)\s+-", line):
            parts = line.split(":", 2)
            if len(parts) >= 3:
                time_range = parts[0] + ":" + parts[1][:5]
                text = line[len(time_range):].strip(" :-\t")
                items.append((time_range.strip(), text))
            else:
                items.append(("", line))
    return items


def md_to_html(md_text: str) -> str:
    """Converts lab markdown scenario/solution text to styled HTML."""
    lines = md_text.splitlines()
    out = []
    in_code = False
    code_buf = []
    in_ol = False
    in_ul = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_code:
                in_code = False
                escaped = html.escape("\n".join(code_buf))
                out.append(f'<pre><code>{escaped}</code></pre>')
                code_buf = []
            else:
                if in_ol: out.append("</ol>"); in_ol = False
                if in_ul: out.append("</ul>"); in_ul = False
                in_code = True
                code_buf = []
            continue

        if in_code:
            code_buf.append(line)
            continue

        if not stripped or stripped.startswith("---") or stripped.startswith("**Date:**") or \
           stripped.startswith("**Session:**") or stripped.startswith("**Time Limit:**") or \
           stripped.startswith("**Target") or stripped.startswith("**Node:**") or \
           stripped.startswith("**Difficulty:**"):
            if in_ol: out.append("</ol>"); in_ol = False
            if in_ul: out.append("</ul>"); in_ul = False
            continue

        if stripped.startswith("# "):
            continue

        if stripped.startswith("### "):
            if in_ol: out.append("</ol>"); in_ol = False
            if in_ul: out.append("</ul>"); in_ul = False
            title = stripped[4:].strip()
            out.append(f'<div class="task-title">📌 {html.escape(title)}</div>')
            continue

        if stripped.startswith("## "):
            if in_ol: out.append("</ol>"); in_ol = False
            if in_ul: out.append("</ul>"); in_ul = False
            title = stripped[3:].strip()
            out.append(f'<div class="section-subhead">{html.escape(title)}</div>')
            continue

        if re.match(r"^[0-9]+\.\s+", stripped):
            if in_ul: out.append("</ul>"); in_ul = False
            if not in_ol: out.append('<ol class="doc-list">'); in_ol = True
            txt = re.sub(r"^[0-9]+\.\s+", "", stripped)
            txt = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", html.escape(txt))
            txt = re.sub(r"`([^`]+)`", r"<code>\1</code>", txt)
            out.append(f'<li>{txt}</li>')
            continue

        if stripped.startswith("- ") or stripped.startswith("* "):
            if in_ol: out.append("</ol>"); in_ol = False
            if not in_ul: out.append('<ul class="doc-list">'); in_ul = True
            txt = stripped[2:]
            txt = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", html.escape(txt))
            txt = re.sub(r"`([^`]+)`", r"<code>\1</code>", txt)
            out.append(f'<li>{txt}</li>')
            continue

        if in_ol: out.append("</ol>"); in_ol = False
        if in_ul: out.append("</ul>"); in_ul = False
        txt = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", html.escape(stripped))
        txt = re.sub(r"`([^`]+)`", r"<code>\1</code>", txt)
        out.append(f'<p>{txt}</p>')

    if in_code:
        out.append(f'<pre><code>{html.escape(chr(10).join(code_buf))}</code></pre>')
    if in_ol: out.append("</ol>")
    if in_ul: out.append("</ul>")
    return "\n".join(out)


def get_day_offset(week: int, day: int) -> int:
    """Computes day offset from START_DATE accounting for the 2-week pause before Week 2."""
    if week == 1:
        return (week - 1) * 7 + (day - 1)
    return (week + 1) * 7 + (day - 1)


def get_shared_css(primary_accent="#0284c7", secondary_accent="#38bdf8", header_gradient=None):
    """Returns CSS styles tailored with specific color accents."""
    if not header_gradient:
        header_gradient = "linear-gradient(135deg, #0f172a 0%, #1e1b4b 55%, #1e3a8a 100%)"
    return f"""
    @page {{
      size: A4 portrait;
      margin: 11mm 11mm 11mm 11mm;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: 'Adwaita Sans', 'Liberation Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 9.3pt;
      line-height: 1.45;
      color: #1e293b;
      background-color: #ffffff;
      margin: 0;
      padding: 0;
    }}
    .page-break {{ page-break-before: always; }}
    .avoid-break {{ break-inside: avoid; page-break-inside: avoid; }}

    .header-banner {{
      background: {header_gradient};
      color: #ffffff;
      padding: 16px 20px;
      border-radius: 9px;
      margin-bottom: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.12);
      border-bottom: 4px solid {secondary_accent};
    }}
    .header-banner h1 {{
      margin: 0 0 4px 0;
      font-size: 19pt;
      font-weight: 800;
      letter-spacing: -0.5px;
    }}
    .header-banner .subtitle {{
      font-size: 10.5pt;
      color: #e2e8f0;
      margin-bottom: 8px;
      font-weight: 600;
    }}
    .badges-row {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 7px;
    }}
    .badge {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 5px;
      font-size: 7.5pt;
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .badge-primary {{ background-color: {primary_accent}; color: #ffffff; }}
    .badge-rec {{ background-color: #059669; color: #ffffff; }}
    .badge-date {{ background-color: #334155; color: #f1f5f9; }}
    .badge-cal {{ background-color: #475569; color: #ffffff; }}

    h2 {{
      font-size: 12.5pt;
      font-weight: 800;
      color: #0f172a;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 3px;
      margin-top: 12px;
      margin-bottom: 8px;
    }}
    .section-title {{ border-bottom-color: {primary_accent}; color: {primary_accent}; }}

    h3 {{
      font-size: 10.2pt;
      font-weight: 700;
      color: #334155;
      margin-top: 10px;
      margin-bottom: 5px;
    }}

    p {{
      margin-top: 0;
      margin-bottom: 6px;
      text-align: justify;
    }}

    .callout {{
      border-radius: 7px;
      padding: 9px 12px;
      margin: 8px 0;
      font-size: 8.6pt;
      line-height: 1.4;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    .callout-info {{ background-color: #f0f9ff; border-left: 4px solid #0284c7; color: #0369a1; }}
    .callout-warning {{ background-color: #fffbeb; border-left: 4px solid #f59e0b; color: #92400e; }}
    .callout-tip {{ background-color: #ecfdf5; border-left: 4px solid #10b981; color: #065f46; }}
    .callout-exam {{ background-color: #fdf2f8; border-left: 4px solid #ec4899; color: #9d174d; }}
    .callout-title {{
      font-weight: bold;
      font-size: 9pt;
      margin-bottom: 4px;
    }}

    .diagram-container {{
      text-align: center;
      margin: 10px 0;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    .diagram-svg {{
      width: 100%;
      max-height: 290px;
      border-radius: 8px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }}

    pre {{
      background-color: #0f172a;
      color: #f8fafc;
      padding: 8px 11px;
      border-radius: 6px;
      font-family: 'JetBrainsMono Nerd Font', 'Adwaita Mono', monospace;
      font-size: 7.8pt;
      line-height: 1.36;
      white-space: pre-wrap;
      word-break: break-word;
      margin: 5px 0 7px 0;
      border: 1px solid #334155;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    code {{
      font-family: 'JetBrainsMono Nerd Font', 'Adwaita Mono', monospace;
      font-size: 8.1pt;
      background-color: #f1f5f9;
      color: #0f172a;
      padding: 1px 3px;
      border-radius: 3px;
      border: 1px solid #cbd5e1;
    }}
    pre code {{
      background-color: transparent;
      color: inherit;
      padding: 0;
      border: none;
      font-size: inherit;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 7px 0;
      font-size: 8pt;
      break-inside: avoid;
      page-break-inside: avoid;
    }}
    th, td {{
      padding: 5px 7px;
      text-align: left;
      border-bottom: 1px solid #e2e8f0;
    }}
    th {{
      background: linear-gradient(135deg, #1e293b, #334155);
      color: #ffffff;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 7pt;
      letter-spacing: 0.5px;
    }}
    tr:nth-child(even) {{ background-color: #f8fafc; }}

    .task-title {{
      font-weight: bold;
      color: #0f172a;
      margin-top: 8px;
      margin-bottom: 3px;
      font-size: 9.2pt;
    }}
    .section-subhead {{
      font-weight: bold;
      color: {primary_accent};
      margin-top: 10px;
      margin-bottom: 4px;
      font-size: 10pt;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 2px;
    }}
    .doc-list {{
      margin: 3px 0 6px 18px;
      padding: 0;
    }}
    .doc-list li {{
      margin-bottom: 3px;
    }}

    .page-footer {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      font-size: 7.2pt;
      color: #94a3b8;
      border-top: 1px solid #e2e8f0;
      padding-top: 2px;
      display: flex;
      justify-content: space-between;
    }}
    """


def render_agenda_card(title, badge_class, time_str, items, bg_color):
    """Renders a timetable card."""
    rows_html = ""
    for t, desc in items:
        rows_html += f"""
        <div style="display: flex; gap: 8px; margin-bottom: 4px; font-size: 8.2pt;">
          <span style="font-family: monospace; font-weight: bold; color: #64748b; white-space: nowrap; min-width: 125px;">{t}</span>
          <span style="color: #1e293b;">{desc}</span>
        </div>
        """
    return f"""
    <div style="background-color: {bg_color}; border: 1px solid #cbd5e1; border-radius: 7px; padding: 10px 12px; margin-bottom: 10px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; border-bottom: 1px solid rgba(0,0,0,0.08); padding-bottom: 5px;">
        <span class="badge {badge_class}">{title}</span>
        <span style="font-size: 8.5pt; font-weight: bold; color: #475569;">🕒 {time_str}</span>
      </div>
      {rows_html}
    </div>
    """


def build_cka_html_for_day(week: int, day: int, schedule_data: dict) -> str:
    """Builds dedicated CKA Daily Study Guide."""
    day_offset = get_day_offset(week, day)
    day_dt = START_DATE + timedelta(days=day_offset)
    date_key = day_dt.strftime("%Y%m%d")
    date_formatted = day_dt.strftime("%A, %B %d, %Y")

    day_info = schedule_data.get(date_key, {})
    events = day_info.get("events", {})

    cka_event = events.get("cka", {})
    rec_event = events.get("recovery", {})

    cka_title = cka_event.get("summary", f"Week {week} Day {day} CKA").replace("[CKA]", "").strip(" :0123456789apmAPM-")
    cka_items = extract_schedule_items(cka_event.get("desc", ""))
    rec_items = extract_schedule_items(rec_event.get("desc", ""))

    curr = get_curriculum(week, day)
    cka_theory_html = curr.get("cka_theory_html", "")
    cka_svg = curr.get("cka_svg", "")
    cka_aliases = curr.get("cka_aliases", "")
    checklist = [item for item in curr.get("checklist", []) if item[0] == "CKA"]

    cka_lab_dir = CKA_DIR / f"w{week}d{day}-cka"
    cka_sc_text = (cka_lab_dir / "scenario.md").read_text(encoding="utf-8") if (cka_lab_dir / "scenario.md").exists() else ""
    cka_so_text = (cka_lab_dir / "solution.md").read_text(encoding="utf-8") if (cka_lab_dir / "solution.md").exists() else ""

    cka_sc_html = md_to_html(cka_sc_text)
    cka_so_html = md_to_html(cka_so_text)

    cka_agenda = render_agenda_card("CKA Morning Deep Dive", "badge-primary", "08:00 AM - 12:00 PM", cka_items, "#f0f9ff")
    rec_agenda = render_agenda_card("Cognitive Recovery & Integration", "badge-rec", "12:00 PM - 03:00 PM", rec_items, "#f8fafc")

    checklist_rows = ""
    for track, competency, verify_cmd in checklist:
        checklist_rows += f"""
        <tr>
          <td><span class="badge badge-primary">{track}</span></td>
          <td>{competency}</td>
          <td><code>{html.escape(verify_cmd)}</code></td>
          <td style="text-align: center; font-weight: bold; color: #059669;">[ &nbsp; ] Ready</td>
        </tr>
        """

    css = get_shared_css(primary_accent="#0284c7", secondary_accent="#38bdf8",
                         header_gradient="linear-gradient(135deg, #0b192c 0%, #1e3a8a 50%, #0284c7 100%)")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CKA Master Daily Study Guide — Week {week} Day {day} ({date_formatted})</title>
  <style>
    {css}
  </style>
</head>
<body>

  <!-- ==================== HEADER BANNER ==================== -->
  <div class="header-banner">
    <div class="badges-row">
      <span class="badge badge-cal">📅 Week {week} Day {day}</span>
      <span class="badge badge-date">{date_formatted}</span>
      <span class="badge badge-primary">☸ CKA Track</span>
      <span class="badge badge-rec">Morning Session</span>
    </div>
    <h1>CKA Master Daily Study Guide</h1>
    <div class="subtitle">{html.escape(cka_title)}</div>
    <div style="font-size: 8.4pt; opacity: 0.95; line-height: 1.35;">
      <strong>Target:</strong> VirtualBox Kubernetes Cluster (<code>controlplane</code>, <code>node01</code>, <code>node02</code>)<br>
      <strong>Orchestrator:</strong> <code>./lab start w{week}d{day}-cka</code> • <code>./lab check w{week}d{day}-cka</code> • <code>./lab solve w{week}d{day}-cka</code>
    </div>
  </div>

  <h2>📅 Morning Time-Blocked Schedule (from cka_lfcs_schedule.ics)</h2>
  <p>
    Adhere strictly to the morning 4-hour block for maximum focus and muscle memory retention on the terminal. Followed by midday cognitive recovery.
  </p>

  {cka_agenda}
  {rec_agenda}

  <!-- ==================== ARCHITECTURAL DEEP DIVE ==================== -->
  <div class="page-break"></div>
  <h2 class="section-title">☸ CKA Architectural Deep Dive: {html.escape(cka_title)}</h2>
  
  {cka_theory_html}

  <div class="diagram-container">
    {cka_svg}
  </div>

  <!-- ==================== HANDS-ON LAB WALKTHROUGH ==================== -->
  <div class="page-break"></div>
  <h2 class="section-title">🛠 Hands-on Lab Walkthrough: w{week}d{day}-cka</h2>
  
  <div class="callout callout-info avoid-break">
    <div class="callout-title">🎯 Lab Scenario Objectives &amp; Tasks</div>
    {cka_sc_html}
  </div>

  <div class="callout callout-tip avoid-break">
    <div class="callout-title">✅ Step-by-Step Grader Solution Walkthrough</div>
    {cka_so_html}
  </div>

  <!-- ==================== EXAM SPEED DRILLS & CHECKLIST ==================== -->
  <div class="page-break"></div>
  <h2 class="section-title">⚡ CKA Speed Drills &amp; Daily Readiness Matrix</h2>

  <div class="callout callout-info avoid-break">
    <div class="callout-title">☸ Essential Kubectl Shortcuts &amp; Terminal Aliases (.bashrc)</div>
    <pre><code>{html.escape(cka_aliases)}</code></pre>
  </div>

  <h3>Daily Self-Assessment Checklist</h3>
  <table class="avoid-break">
    <thead>
      <tr>
        <th style="width: 10%;">Track</th>
        <th style="width: 48%;">Core Competency / Question</th>
        <th style="width: 30%;">Verification Command</th>
        <th style="width: 12%;">Mastery</th>
      </tr>
    </thead>
    <tbody>
      {checklist_rows}
    </tbody>
  </table>

  <!-- Footer -->
  <div class="page-footer">
    <span>CKA Official Preparation Guide • Week {week} Day {day}</span>
    <span>Orchestrator: <code>./lab check w{week}d{day}-cka</code></span>
  </div>

</body>
</html>
"""


def build_lfcs_html_for_day(week: int, day: int, schedule_data: dict) -> str:
    """Builds dedicated LFCS Daily Study Guide."""
    day_offset = get_day_offset(week, day)
    day_dt = START_DATE + timedelta(days=day_offset)
    date_key = day_dt.strftime("%Y%m%d")
    date_formatted = day_dt.strftime("%A, %B %d, %Y")

    day_info = schedule_data.get(date_key, {})
    events = day_info.get("events", {})

    lfcs_event = events.get("lfcs", {})
    rec_event = events.get("recovery", {})

    lfcs_title = lfcs_event.get("summary", f"Week {week} Day {day} LFCS").replace("[LFCS]", "").strip(" :0123456789apmAPM-")
    lfcs_items = extract_schedule_items(lfcs_event.get("desc", ""))
    rec_items = extract_schedule_items(rec_event.get("desc", ""))

    curr = get_curriculum(week, day)
    lfcs_theory_html = curr.get("lfcs_theory_html", "")
    lfcs_svg = curr.get("lfcs_svg", "")
    lfcs_aliases = curr.get("lfcs_aliases", "")
    checklist = [item for item in curr.get("checklist", []) if item[0] == "LFCS"]

    lfcs_lab_dir = LFCS_DIR / f"w{week}d{day}-lfcs"
    lfcs_sc_text = (lfcs_lab_dir / "scenario.md").read_text(encoding="utf-8") if (lfcs_lab_dir / "scenario.md").exists() else ""
    lfcs_so_text = (lfcs_lab_dir / "solution.md").read_text(encoding="utf-8") if (lfcs_lab_dir / "solution.md").exists() else ""

    lfcs_sc_html = md_to_html(lfcs_sc_text)
    lfcs_so_html = md_to_html(lfcs_so_text)

    rec_agenda = render_agenda_card("Cognitive Recovery & Integration", "badge-rec", "12:00 PM - 03:00 PM", rec_items, "#f8fafc")
    lfcs_agenda = render_agenda_card("LFCS Afternoon Mastery", "badge-primary", "03:00 PM - 06:00 PM", lfcs_items, "#fffbeb")

    checklist_rows = ""
    for track, competency, verify_cmd in checklist:
        checklist_rows += f"""
        <tr>
          <td><span class="badge badge-primary">{track}</span></td>
          <td>{competency}</td>
          <td><code>{html.escape(verify_cmd)}</code></td>
          <td style="text-align: center; font-weight: bold; color: #059669;">[ &nbsp; ] Ready</td>
        </tr>
        """

    css = get_shared_css(primary_accent="#d97706", secondary_accent="#f59e0b",
                         header_gradient="linear-gradient(135deg, #1c1917 0%, #78350f 50%, #d97706 100%)")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>LFCS Master Daily Study Guide — Week {week} Day {day} ({date_formatted})</title>
  <style>
    {css}
  </style>
</head>
<body>

  <!-- ==================== HEADER BANNER ==================== -->
  <div class="header-banner">
    <div class="badges-row">
      <span class="badge badge-cal">📅 Week {week} Day {day}</span>
      <span class="badge badge-date">{date_formatted}</span>
      <span class="badge badge-primary">🐧 LFCS Track</span>
      <span class="badge badge-rec">Afternoon Session</span>
    </div>
    <h1>LFCS Master Daily Study Guide</h1>
    <div class="subtitle">{html.escape(lfcs_title)}</div>
    <div style="font-size: 8.4pt; opacity: 0.95; line-height: 1.35;">
      <strong>Target:</strong> VirtualBox Linux Machine (<code>LFCS</code>)<br>
      <strong>Orchestrator:</strong> <code>./lab start w{week}d{day}-lfcs</code> • <code>./lab check w{week}d{day}-lfcs</code> • <code>./lab solve w{week}d{day}-lfcs</code>
    </div>
  </div>

  <h2>📅 Afternoon Time-Blocked Schedule (from cka_lfcs_schedule.ics)</h2>
  <p>
    Structured afternoon 3-hour Linux administration deep dive. Begin with cognitive integration review.
  </p>

  {rec_agenda}
  {lfcs_agenda}

  <!-- ==================== CORE CONCEPTS DEEP DIVE ==================== -->
  <div class="page-break"></div>
  <h2 class="section-title">🐧 LFCS Core Concepts Deep Dive: {html.escape(lfcs_title)}</h2>
  
  {lfcs_theory_html}

  <div class="diagram-container">
    {lfcs_svg}
  </div>

  <!-- ==================== HANDS-ON LAB WALKTHROUGH ==================== -->
  <div class="page-break"></div>
  <h2 class="section-title">🛠 Hands-on Lab Walkthrough: w{week}d{day}-lfcs</h2>
  
  <div class="callout callout-warning avoid-break">
    <div class="callout-title">🎯 Lab Scenario Objectives &amp; Tasks</div>
    {lfcs_sc_html}
  </div>

  <div class="callout callout-tip avoid-break">
    <div class="callout-title">✅ Step-by-Step Grader Solution Walkthrough</div>
    {lfcs_so_html}
  </div>

  <!-- ==================== EXAM SPEED DRILLS & CHECKLIST ==================== -->
  <div class="page-break"></div>
  <h2 class="section-title">⚡ LFCS Speed Drills &amp; Daily Readiness Matrix</h2>

  <div class="callout callout-warning avoid-break">
    <div class="callout-title">🐧 Essential Linux CLI Shortcuts &amp; Terminal Aliases (.bashrc)</div>
    <pre><code>{html.escape(lfcs_aliases)}</code></pre>
  </div>

  <h3>Daily Self-Assessment Checklist</h3>
  <table class="avoid-break">
    <thead>
      <tr>
        <th style="width: 10%;">Track</th>
        <th style="width: 48%;">Core Competency / Question</th>
        <th style="width: 30%;">Verification Command</th>
        <th style="width: 12%;">Mastery</th>
      </tr>
    </thead>
    <tbody>
      {checklist_rows}
    </tbody>
  </table>

  <!-- Footer -->
  <div class="page-footer">
    <span>LFCS Official Preparation Guide • Week {week} Day {day}</span>
    <span>Orchestrator: <code>./lab check w{week}d{day}-lfcs</code></span>
  </div>

</body>
</html>
"""


def compile_pdf(html_path: Path, pdf_path: Path) -> bool:
    """Compiles HTML file to PDF via headless Chromium/Chrome if available."""
    import shutil
    browser = None
    for candidate in ["google-chrome-stable", "google-chrome", "chromium", "chromium-browser", "brave", "brave-browser"]:
        if shutil.which(candidate):
            browser = candidate
            break
    if not browser:
        return False

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-extensions",
        "--user-data-dir=/tmp/pdf_chromium_profile",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        str(html_path)
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        return res.returncode == 0
    except Exception:
        return False


def generate_single_day(week: int, day: int, schedule_data: dict, track: str = "both", verbose: bool = True):
    """Generates track-separated study guides for a single day."""
    day_offset = get_day_offset(week, day)
    day_dt = START_DATE + timedelta(days=day_offset)
    date_key = day_dt.strftime("%Y%m%d")

    generated = []

    # CKA Guide
    if track in ["both", "cka"]:
        cka_html = build_cka_html_for_day(week, day, schedule_data)
        out_html = CKA_GUIDES_DIR / f"CKA_Daily_Study_Guide_W{week}D{day}_{date_key}.html"
        out_pdf = CKA_GUIDES_DIR / f"CKA_Daily_Study_Guide_W{week}D{day}_{date_key}.pdf"
        out_html.write_text(cka_html, encoding="utf-8")
        compile_pdf(out_html, out_pdf)
        generated.append(out_html)
        if verbose:
            sz_kb = out_html.stat().st_size / 1024
            print(f"[✓] CKA  W{week}D{day} -> {out_html.name} ({sz_kb:.1f} KB)")

    # LFCS Guide
    if track in ["both", "lfcs"]:
        lfcs_html = build_lfcs_html_for_day(week, day, schedule_data)
        out_html = LFCS_GUIDES_DIR / f"LFCS_Daily_Study_Guide_W{week}D{day}_{date_key}.html"
        out_pdf = LFCS_GUIDES_DIR / f"LFCS_Daily_Study_Guide_W{week}D{day}_{date_key}.pdf"
        out_html.write_text(lfcs_html, encoding="utf-8")
        compile_pdf(out_html, out_pdf)
        generated.append(out_html)
        if verbose:
            sz_kb = out_html.stat().st_size / 1024
            print(f"[✓] LFCS W{week}D{day} -> {out_html.name} ({sz_kb:.1f} KB)")

    return generated


def generate_day_worker(args):
    week, day, schedule_data, track = args
    return generate_single_day(week, day, schedule_data, track=track, verbose=False)


def main():
    schedule = parse_ics_schedule(ICS_PATH)
    args = sys.argv[1:]

    track = "both"
    clean_args = []
    for a in args:
        if a.lower() in ["--cka", "-cka"]:
            track = "cka"
        elif a.lower() in ["--lfcs", "-lfcs"]:
            track = "lfcs"
        elif a.lower() in ["--both", "-both"]:
            track = "both"
        else:
            clean_args.append(a)

    if not clean_args:
        print("[*] No day specified. Generating default Day 1 (W1D1)...")
        generate_single_day(1, 1, schedule, track=track)
        return

    first_arg = clean_args[0].lower().strip("-")

    # Generate ALL 48 days
    if first_arg in ["all"]:
        print(f"[*] Starting batch generation for ALL 48 DAYS (Weeks 1 to 8, Track: {track})...")
        tasks = []
        for w in range(1, 9):
            for d in range(1, 7):
                tasks.append((w, d, schedule, track))

        start_t = datetime.now()
        completed = 0
        with ProcessPoolExecutor(max_workers=4) as executor:
            future_to_day = {executor.submit(generate_day_worker, t): (t[0], t[1]) for t in tasks}
            for future in as_completed(future_to_day):
                w, d = future_to_day[future]
                try:
                    res = future.result()
                    completed += 1
                    names = ", ".join(f.name for f in res)
                    print(f"[{completed:02d}/48] [✓] Week {w} Day {d} -> {names}")
                except Exception as e:
                    print(f"[-] Error on Week {w} Day {d}: {e}", file=sys.stderr)

        elapsed = (datetime.now() - start_t).total_seconds()
        print(f"\n[★] Batch generation complete in {elapsed:.1f}s!")
        print(f"    CKA Guides:  {CKA_GUIDES_DIR}")
        print(f"    LFCS Guides: {LFCS_GUIDES_DIR}")
        return

    # Generate specific week
    if first_arg in ["week", "w"] and len(clean_args) > 1:
        wk = int(clean_args[1])
        print(f"[*] Generating all 6 study days for Week {wk} (Track: {track})...")
        for d in range(1, 7):
            generate_single_day(wk, d, schedule, track=track)
        return

    # Specific day notation: wXdY (e.g. w1d1)
    m = re.match(r"^w([1-8])d([1-6])$", first_arg)
    if m:
        wk = int(m.group(1))
        dy = int(m.group(2))
        generate_single_day(wk, dy, schedule, track=track)
        return

    print(f"[-] Unrecognized option: {' '.join(args)}")
    print("Usage:")
    print("  python3 generate_daily_guide.py w1d1              # Generate both CKA & LFCS for W1D1")
    print("  python3 generate_daily_guide.py w1d1 --cka        # Generate only CKA guide")
    print("  python3 generate_daily_guide.py w1d1 --lfcs       # Generate only LFCS guide")
    print("  python3 generate_daily_guide.py --week 1          # Generate Week 1")
    print("  python3 generate_daily_guide.py --all             # Generate ALL 48 daily guides")


if __name__ == "__main__":
    main()
