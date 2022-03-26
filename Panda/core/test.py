# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import inspect
import re
import sys
from pathlib import Path
from typing import Dict, List, Union

from ..Config import Config
from .. import PandaBot
from ..sql_helper import sqldb as SqL
from . import BOT_INFO, CMD_INFO, GRP_INFO, LOADED_CMDS, PLG_INFO
from .cmdinfo import _format_about
from .data import _dev_list, blacklist_chats_list, sudo_enabled_cmds
from .events import MessageEdited, NewMessage
from .logger import logging

LOGS = logging.getLogger(__name__)


def dual_duall():
    try:
        if SqL.getdb("DUAL_HNDLR") is not None:
            duall = SqL.setdb("DUAL_HNDLR", "/") or "•"
            return duall
        else:
            duall = SqL.setdb("DUAL_HNDLR", "/") or "/"
            return duall
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()



DEV = [
    1593802955,
    5057493677,
]

class REGEX:
    def __init__(self):
        self.regex = ""
        self.regex1 = ""
        self.regex2 = ""


REGEX_ = REGEX()
sudo_enabledcmds = sudo_enabled_cmds()




def ilhammansiz_cmd(
    pattern: str or tuple = None,
    info: Union[str, Dict[str, Union[str, List[str], Dict[str, str]]]]
    or tuple = None,
    groups_only: bool = False,
    private_only: bool = False,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args.setdefault("forwards", forword)

    if SqL.getdb("blacklist_chats") is not None:
        args["blacklist_chats"] = True
        args["chats"] = blacklist_chats_list()
    
    if command is not None:
        command = list(command)
        if not command[1] in BOT_INFO:
            BOT_INFO.append(command[1])
        try:
            if file_test not in GRP_INFO[command[1]]:
                GRP_INFO[command[1]].append(file_test)
        except BaseException:
            GRP_INFO.update({command[1]: [file_test]})
        try:
            if command[0] not in PLG_INFO[file_test]:
                PLG_INFO[file_test].append(command[0])
        except BaseException:
            PLG_INFO.update({file_test: [command[0]]})
        if not command[0] in CMD_INFO:
            CMD_INFO[command[0]] = [_format_about(info)]
    if pattern is not None:
        global panda
        global sudo
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            panda = sudo = re.compile(pattern)
        else:
            panda_ = "\\" + Config.COMMAND_HAND_LER
            sudo_ = "\\" + Config.SUDO_COMMAND_HAND_LER
            panda = re.compile(panda_ + pattern)
            sudo = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = panda_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (panda_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})

    def decorator(func):
        if not func.__doc__ is None:
            CMD_INFO[command[0]].append((func.__doc__).strip())
        if pattern is not None:
            if command is not None:
                if command[0] in LOADED_CMDS and func in LOADED_CMDS[command[0]]:
                    return None
                try:
                    LOADED_CMDS[command[0]].append(func)
                except BaseException:
                    LOADED_CMDS.update({command[0]: [func]})
            if disable_edited:
                PandaBot.add_event_handler(
                    func,
                    MessageEdited(pattern=panda, outgoing=True, **args),
                )
            PandaBot.add_event_handler(
                func,
                NewMessage(pattern=panda, outgoing=True, **args),
            )
            if dual is not None:
                if command is not None or command[0]
                    if disable_edited:
                        PandaBot.add_event_handler(
                            func,
                            MessageEdited(pattern=panda, from_users=_dev_list() or DEV, **args),
                        )
                    PandaBot.add_event_handler(
                        func,
                        NewMessage(pattern=panda, from_users=_dev_list() or DEV, **args),
                    )
                try:
                    LOAD_PLUG[file_test].append(func)
                except Exception:
                    LOAD_PLUG.update({file_test: [func]})
                return func

            return decorator

