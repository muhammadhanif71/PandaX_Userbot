from . import db_x

gmuteh = db_x["GMUTE"]


def is_gmuted(sender_id):
    kk = gmuteh.find_one({"sender_id": sender_id})
    if not kk:
        return False
    else:
        return True


def gmute(sender_id, reason="#GMuted"):
    return gmuteh.insert_one({"sender_id": sender_id, "reason": reason})


def ungmute(sender_id):
    return gmuteh.delete_one({"sender_id": sender_id})

