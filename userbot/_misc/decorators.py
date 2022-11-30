# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery
import ublackdev
from ..Var import Config
Alive = Config.ALIVE_NAME
DEVLIST = [1027174031, 5615921474]


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id in Config.SUDO_USERS:
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModifiedError:
                pass
        else:
            await c_q.answer(
                f"𝐌𝐞𝐧𝐮 𝐇𝐞𝐥𝐩 || 𝐎𝐰𝐧𝐞𝐫: {Alive}\n\n𝗖𝗿𝗲𝗮𝘁𝗲 𝗯𝗼𝘁 𝗝𝗼𝗶𝗻 @𝐬𝐭𝐮𝐟𝐩𝐩𝐨𝐫𝐭",
                alert=True,
            )

    return wrapper
