
from .. import SqL




def add_welcome(chat_id, message_id):
    stark = SqL.getdb("chat_id")
    if stark:
        SqL.setdb("chat_id", message_id)
    else:
        SqL.setdb("chat_id", message_id)


def del_welcome(chat_id):
    SqL.deldb("chat_id")


def welcome_info(chat_id):
    r = SqL.getdb("chat_id")
    if r:
        return r
    else:
        return False
