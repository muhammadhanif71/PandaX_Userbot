from .. import SqL


try:
    eval(SqL.getdb("FILTER"))
except BaseException:
    SqL.setdb("FILTER", "{}")




def add_filters(keyword, chat_id, message_id) -> None:
    ok = eval(SqL.getdb("FILTER"))
    ok.update({chat_id: {"keyword": keyword, "chat_id": chat_id, "msg_id": message_id}})
    return SqL.setdb("FILTER", ok)


def filters_info(keyword, chat_id):
    ok = eval(SqL.getdb("FILTER"))
    wl = ok.get(chat_id)
    if wl:
        return wl
    return


def del_filters(keyword, chat_id):
    ok = eval(SqL.getdb("FILTER"))
    wl = ok.get(chat_id)
    if wl:
        ok.pop(chat_id)
        return SqL.setdb("FILTER", ok)
    return


def filters_del(chat_id):
    ok = eval(SqL.getdb("FILTER"))
    wk = ok.get(chat_id)
    if wk:
        ok.pop(chat_id)
        return SqL.setdb("FILTER", ok)
    return

def all_filters(chat_id):
    ok = eval(SqL.getdb("FILTER"))
    if ok.get(chat_id):
        return ok
    else:
        return False
    
