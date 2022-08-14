"""
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

"""

try:
    from ..sql_helper import BASE, SESSION
except ImportError:
    raise AttributeError

from sqlalchemy import BigInteger, Column, Numeric, String, UnicodeText


class PyroWelcome(BASE):
    __tablename__ = "joinwelcome"
    chat_id = Column(String(14), primary_key=True)
    message_id = Column(BigInteger)
    message_id = Column(UnicodeText)
    message_id = Column(Numeric)

    def __init__(self, chat_id, message_id):
        self.chat_id = str(chat_id)
        self.message_id = message_id
        
PyroWelcome.__table__.create(checkfirst=True)


def welcome_info(chat_id):
    try:
        return SESSION.query(PyroWelcome).get(str(chat_id))
    finally:
        SESSION.close()


def getcurrent_welcome_settings(chat_id):
    try:
        return (
            SESSION.query(PyroWelcome).filter(PyroWelcome.chat_id == str(chat_id)).one()
        )
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_welcome(chat_id, message_id):
    to_check = welcome_info(chat_id)
    if not to_check:
        adder = PyroWelcome(chat_id, message_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    rem = SESSION.query(PyroWelcome).get(str(chat_id))
    SESSION.delete(rem)
    SESSION.commit()
    adder = PyroWelcome(chat_id, message_id)
    SESSION.commit()
    return False


def del_welcome(chat_id):
    try:
        rem = SESSION.query(PyroWelcome).get(str(chat_id))
        if rem:
            SESSION.delete(rem)
            SESSION.commit()
            return True
    except BaseException:
        return False


def updateprevious_welcome(chat_id, message_id):
    row = SESSION.query(PyroWelcome).get(str(chat_id))
    row.message_id = message_id
    SESSION.commit()
