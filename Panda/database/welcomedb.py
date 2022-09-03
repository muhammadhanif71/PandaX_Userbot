
from .. import SqL


try:
    eval(SqL.getdb("WELCOME"))
except BaseException:
    SqL.setdb("WELCOME", "{}")




def add_welcome(chat_id, msg, media):
    ok = eval(SqL.getdb("WELCOME"))
    ok.update({chat_id: {"msg_id": message_id}})
    return SqL.setdb("WELCOME", str(ok))


def welcome_info(chat_id):
    ok = eval(SqL.getdb("WELCOME"))
    wl = ok.get(chat_id)
    if wl:
        return wl
    return


def del_welcome(chat_id):
    ok = eval(SqL.getdb("WELCOME"))
    wl = ok.get(chat_id)
    if wl:
        ok.pop(chat_id)
        return SqL.setdb("WELCOME", str(ok))
    return

