from .. import SqL

def get_stuff(key=None):
    return SqL.getdb(key) or {}


def add_welcome(chat_id, message_id):
    ok = get_stuff("WELCOME")
    ok.update({"chat_id": chat_id, "msg_id": message_id})
    return SqL.setdb("WELCOME", ok)


def del_welcome(chat_id):
    ok = get_stuff("WELCOME")
    if ok.get(chat_id):
        ok.pop(chat_id)
        return SqL.setdb("WELCOME", ok)

def welcome_info(chat_id):
    ok = get_stuff("WELCOME")
    return ok.get(chat_id)
