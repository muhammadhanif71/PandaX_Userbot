
from .pyroclient import pyrotgbot, pyrobot
from telethon import functions, utils

import logging
from ..Var import Var
from logging import getLogger
import pyrogram as pandapyro
from .._func.startup import load_modulesPyro, plugin_collecter
from .pyroclient import pyrobot, pyrobot2, pyrobot3, pyrobot4, pyrotgbot
import sys
LOGS = getLogger(__name__)



def Pyrogram():
    if pyrotgbot:
        pyrotgbot.start()
        pyrotgbot.me = pyrotgbot.get_me()
        assistant_mods = plugin_collecter("./assistant/")
        for mods in assistant_mods:
            try:
                load_modulesPyro(mods, assistant=True)
            except Exception as e:
                logging.error("[ASSISTANT] - Failed To Load : " + f"{mods} - {str(e)}")
    if pyrobot:
        pyrobot.start()
        pyrobot.me = pyrobot.get_me()
        pyrobot.has_a_bot = True if pyrotgbot else False
    if pyrobot2:
        pyrobot2.start()
        pyrobot2.me = pyrobot2.get_me()
        pyrobot2.has_a_bot = True if pyrotgbot else False
    if pyrobot3:
        pyrobot3.start()
        pyrobot3.me = pyrobot3.get_me()
        pyrobot3.has_a_bot = True if pyrotgbot else False
    if pyrobot4:
        pyrobot4.start()
        pyrobot.me = pyrobot4.get_me()
        pyrobot4.has_a_bot = True if pyrotgbot else False
    needed_mods = plugin_collecter("./ModulesPyro/")
    for nm in needed_mods:
        try:
            load_modulesPyro(nm)
        except Exception as e:
            logging.error("[USER] - Failed To Load : " + f"{nm} - {str(e)}")
    pandapyro.idle()
