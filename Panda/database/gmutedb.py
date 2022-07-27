"""
from . import db_x as SqL


def list_gmuted():
    return SqL.getdb("GMUTE") or []

def gmute(user):
    ok = list_gmuted()
    ok.append(int(user))
    return SqL.setdb("GMUTE", ok)


def ungmute(user):
    ok = list_gmuted()
    if user in ok:
        ok.remove(int(user))
        return SqL.setdb("GMUTE", ok)

def is_gmuted(user):
    return int(user) in list_gmuted()

"""

from ..sql_helper.mute_sql import is_muted, mute, unmute
from ..sql_helper.gban_sql_helper import get_all_gbanned


is_gmuted = is_muted
ungmute = unmute
gmute = mute
list_gmuted = get_all_gbanned
