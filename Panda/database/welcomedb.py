
from .. import SqL




def get_stuff(key=None):
    return SqL.getdb(key) or {}


def add_welcome(chat_id, message_id):
    ok = get_stuff("WELCOME")
    ok.update({chat_id: {"msg_id": message_id}})
    return SqL.setdb("WELCOME", ok)


def get_welcome(chat):
    ok = get_stuff("WELCOME")
    return ok.get(chat)


def welcome_info(chat):
    ok = get_stuff("WELCOME")
    if ok.get(chat):
        ok.pop(chat)
        return SqL.setdb("WELCOME", ok)
