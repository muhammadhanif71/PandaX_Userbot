from ..sql_helper.db import BaseDB as SqL


def get_stuff():
    return SqL.getdb("NOTE") or {}


def add_note(keyword, chat_id, message_id):
    ok = get_stuff()
    if ok.get(int(chat_id)):
        ok[int(chat_id)].update({"keyword": keyword, "chat_id": chat_id, "msg_id": message_id})
    else:
        ok.update({"keyword": keyword, "chat_id": chat_id, "msg_id": message_id})
    SqL.setdb("NOTE", ok)


def del_note(chat_id, keyword):
    ok = get_stuff()
    if ok.get(int(chat_id)) and ok[int(chat_id)].get(keyword):
        ok[int(chat_id)].pop(keyword)
        return SqL.setdb("NOTE", ok)


def del_notes(chat_id):
    ok = get_stuff()
    if ok.get(int(chat_id)):
        ok.pop(int(chat_id))
        return SqL.setdb("NOTE", ok)


def note_info(chat_id, keyword):
    ok = get_stuff()
    if ok.get(int(chat_id)) and ok[int(chat_id)].get(keyword):
        return ok[int(chat_id)][keyword]


def all_note(chat_id):
    ok = get_stuff()
    if ok.get(int(chat_id)):
        return "".join(f"🤗 #{z}\n" for z in ok[chat_id])

