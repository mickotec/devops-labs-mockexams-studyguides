"""LFCS Dedicated Curriculum Package"""
from . import week1
from . import week2
from . import week3
from . import week4
from . import week5
from . import week6
from . import week7
from . import week8

WEEKS = {
    1: week1,
    2: week2,
    3: week3,
    4: week4,
    5: week5,
    6: week6,
    7: week7,
    8: week8,
}

def get_curriculum(week: int, day: int) -> dict:
    wk_mod = WEEKS.get(week, week1)
    return wk_mod.get_day_content(day)
