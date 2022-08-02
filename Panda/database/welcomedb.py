from .. import SqL

def get_stuff(key=None):
    return SqL.getdb(key) or {}


def add_welcome(chat_id, message_id):
    ok = get_stuff("WELCOME")
    ok.update({chat: {{"chat_id": chat_id, "msg_id": message_id})
    return SqL.setdb("WELCOME", ok)


