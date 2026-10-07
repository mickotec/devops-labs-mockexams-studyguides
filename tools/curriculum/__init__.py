"""
CKA & LFCS Master Curriculum Package
Dispatches day content (theory, SVG vector diagrams, aliases, and checklists)
to dedicated CKA and LFCS subpackages for all 8 weeks (48 active days).
"""

import re
from . import cka
from . import lfcs

class _MergedWeek:
    """Wrapper that merges CKA and LFCS daily content and exposes day methods and docstrings."""
    def __init__(self, week_num: int, cka_week, lfcs_week):
        self.week_num = week_num
        self.cka_week = cka_week
        self.lfcs_week = lfcs_week
        
        doc_lines = [f"Curriculum Content: Week {week_num} (Days 1 to 6)"]
        for d in range(1, 7):
            cka_topic = "CKA Study"
            lfcs_topic = "LFCS Study"
            if cka_week and cka_week.__doc__:
                for line in cka_week.__doc__.splitlines():
                    m = re.match(r"Day\s+(\d+):\s*(.*)", line.strip())
                    if m and int(m.group(1)) == d:
                        cka_topic = m.group(2).strip()
            if lfcs_week and lfcs_week.__doc__:
                for line in lfcs_week.__doc__.splitlines():
                    m = re.match(r"Day\s+(\d+):\s*(.*)", line.strip())
                    if m and int(m.group(1)) == d:
                        lfcs_topic = m.group(2).strip()
            doc_lines.append(f"Day {d}: {cka_topic} | {lfcs_topic}")
        self.__doc__ = "\n".join(doc_lines)

    def get_day_content(self, day: int) -> dict:
        c = self.cka_week.get_day_content(day) if (self.cka_week and hasattr(self.cka_week, "get_day_content")) else {}
        l = self.lfcs_week.get_day_content(day) if (self.lfcs_week and hasattr(self.lfcs_week, "get_day_content")) else {}
        return {
            "cka_theory_html": c.get("cka_theory_html", c.get("theory_html", "")),
            "cka_svg": c.get("cka_svg", c.get("svg", "")),
            "cka_aliases": c.get("cka_aliases", c.get("aliases", "")),
            "lfcs_theory_html": l.get("lfcs_theory_html", l.get("theory_html", "")),
            "lfcs_svg": l.get("lfcs_svg", l.get("svg", "")),
            "lfcs_aliases": l.get("lfcs_aliases", l.get("aliases", "")),
            "checklist": c.get("checklist", []) + l.get("checklist", []),
        }

    def __getattr__(self, name: str):
        if name.startswith("get_day_"):
            try:
                day_num = int(name.split("_")[-1])
                return lambda: self.get_day_content(day_num)
            except ValueError:
                pass
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")


WEEKS = {
    w: _MergedWeek(w, cka.WEEKS.get(w), lfcs.WEEKS.get(w))
    for w in range(1, 9)
}

def get_curriculum(week: int, day: int, track: str = None) -> dict:
    """Returns theory, SVG diagrams, and checklists for given (week, day).
    If track is 'cka' or 'lfcs', delegates directly to the dedicated track.
    If track is None, returns merged content for both tracks.
    """
    if track:
        tr = track.strip().lower()
        if tr == "lfcs":
            return lfcs.get_curriculum(week, day)
        elif tr == "cka":
            return cka.get_curriculum(week, day)

    wk_obj = WEEKS.get(week)
    if wk_obj:
        return wk_obj.get_day_content(day)
    return {}
