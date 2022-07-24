from .. import SqL


def list_gmuted():
    return SqL.getdb("GMUTE") or []

def gmute(user):
    ok = list_gmuted()
    ok.append(int(user))
    return SqL.getdb("GMUTE", ok)


def ungmute(user):
    ok = list_gmuted()
    if user in ok:
        ok.remove(int(user))
        return SqL.getdb("GMUTE", ok)

def is_gmuted(user):
    return int(user) in list_gmuted()



