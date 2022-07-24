from . import db_x

gbun = db_x["GBAN"]


def gban_user(user, reason="#GBanned"):
    return gbun.insert_one({"user": user, "reason": reason})


def ungban_user(user):
    return gbun.delete_one({"user": user})


def gban_list():
    return [lo async for lo in gbun.find({})]


def gban_info(user):
    kk = gbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
