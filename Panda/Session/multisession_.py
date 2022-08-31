
from .pyroclient import pyrotgbot, pyrobot
from telethon import functions, utils

import logging
from ..Var import Var
from logging import getLogger
import pyrogram as pandapyro
from .client import PandaBot, PandaBot2, PandaBot3, tgbot
from .._func.startup import load_modulesPyro, plugin_collecter
from .pyroclient import pyrobot, pyrobot2, pyrobot3, pyrobot4, pyrotgbot
import sys
LOGS = getLogger(__name__)
import os
from pyrogram import __version__ as pyrover

PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    
cmdhr = os.environ.get("COMMAND_HAND_LER") or "."
    
MSG_ON = """
꧁༺ Panda Userbot ༻꧂
━━
⚙️ Pyrogram Version - `{}'
°Ketik `{}alive` untuk Mengecheck Bot
━━
"""

def Telethon():
    if Var.STRING_SESSION:
        try:
            PandaBot.start()
            delta = PandaBot(functions.help.GetConfigRequest())
            for option in delta.dc_options:
                if option.ip_address == PandaBot.session.server_address:
                    if PandaBot.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot.session.dc_id}"
                            f" to {option.id}"
                        )
                    PandaBot.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot.session.save()
                    break
            PandaBot.me = PandaBot.get_me()
            tgbot.get_me()
            PandaBot.uid = tgbot.uid = utils.get_peer_id(PandaBot.me)
            if Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot.me)
        except Exception as e:
            LOGS.error(f"STRING_SESSION - {str(e)}")
            sys.exit()


    if Var.STRING_SESSION2:
        try:
            PandaBot2.start()
            delta = PandaBot2(functions.help.GetConfigRequest())
            for option in delta.dc_options:
                if option.ip_address == PandaBot2.session.server_address:
                    if PandaBot2.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot2.session.dc_id}"
                            f" to {option.id}"
                        )
                    PandaBot2.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot2.session.save()
                    break
            PandaBot2.me = PandaBot2.get_me()
            tgbot.get_me()
            PandaBot.uid = tgbot.uid = utils.get_peer_id(PandaBot2.me)
            if Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot2.me)
        except Exception as e:
            LOGS.error(f"STRING_SESSION - {str(e)}")
            sys.exit()
     
    if Var.STRING_SESSION3:
        try:
            PandaBot3.start()
            delta = PandaBot3(functions.help.GetConfigRequest())
            for option in delta.dc_options:
                if option.ip_address == PandaBot3.session.server_address:
                    if PandaBot3.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {PandaBot3.session.dc_id}"
                            f" to {option.id}"
                        )
                    PandaBot3.session.set_dc(option.id, option.ip_address, option.port)
                    PandaBot3.session.save()
                    break
            PandaBot3.me = PandaBot3.get_me()
            tgbot.get_me()
            PandaBot.uid = tgbot.uid = utils.get_peer_id(PandaBot.me)
            if Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(PandaBot3.me)
        except Exception as e:
            LOGS.error(f"STRING_SESSION - {str(e)}")
            sys.exit()


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
    if pyrobot:
        pyrobot.send_message(PRIVATE_GROUP_BOT_API_ID, MSG_ON.format(pyrover, cmdhr))
    if pyrobot2:
        pyrobot2.send_message(PRIVATE_GROUP_BOT_API_ID, MSG_ON.format(pyrover, cmdhr))
    if pyrobot3:
        pyrobot3.send_message(PRIVATE_GROUP_BOT_API_ID, MSG_ON.format(pyrover, cmdhr))
    if pyrobot4:
        pyrobot4.send_message(PRIVATE_GROUP_BOT_API_ID, MSG_ON.format(pyrover, cmdhr))
    LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ PyroVersion:{pyrover} [TELAH DIAKTIFKAN]")
    pandapyro.idle()
