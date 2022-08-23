## Copyright Panda Userbot
## Recode by Ilham Mansiz


from datetime import datetime

from pyrogram import filters

from Panda._func.decorators import Panda_cmd, listen
import asyncio
from datetime import datetime
from pyrogram.types import Message

import humanize
from pyrogram import filters

from . import HELP


HELP(
    "afk",
)

def GetChatID(message: Message):
    """ Get the group id of the incoming message"""
    return message.chat.id



AFK = False
AFK_REASON = ""
AFK_TIME = ""
USERS = {}
GROUPS = {}


def subtract_time(start, end):
    """Get humanized time"""
    subtracted = humanize.naturaltime(start - end)
    return str(subtracted)



@listen(
    (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.bot
    & ~filters.service
    & ~filters.edited
    & filters.incoming
)
async def collect_afk_messages(client, message):
    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME)
        is_group = True if message.chat.type in ["supergroup", "group"] else False
        CHAT_TYPE = GROUPS if is_group else USERS

        if GetChatID(message) not in CHAT_TYPE:
            text = (
                f"┌ 🐍 AFK\n"
                f"│┌ Saya Sedang AFK\n"
                f"│├ {last_seen} Yang Lalu \n"
                f"└└ Alasan: ```{AFK_REASON.upper()}```"
            )
            await client.send_message(
                chat_id=GetChatID(message),
                text=text,
                reply_to_message_id=message.message_id,
            )
            CHAT_TYPE[GetChatID(message)] = 1
            return
        elif GetChatID(message) in CHAT_TYPE:
            if CHAT_TYPE[GetChatID(message)] == 50:
                text = (
                    f"┌ 🐍 AFK\n"
                    f"│┌ Saya Sedang AFK\n"
                    f"│├ {last_seen} Yang Lalu \n"
                    f"└└ Alasan: ```{AFK_REASON.upper()}```"
                )
                await client.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=message.message_id,
                )
            elif CHAT_TYPE[GetChatID(message)] > 50:
                return
            elif CHAT_TYPE[GetChatID(message)] % 5 == 0:
                text = (
                    f"┌ 🐍 AFK\n"
                    f"│┌ Saya Sedang tidak AFK\n"
                    f"│├ {last_seen} Yang Lalu \n"
                    f"└└ Alasan: ```{AFK_REASON.upper()}```"
                )
                await client.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=message.message_id,
                )

        CHAT_TYPE[GetChatID(message)] += 1


@Panda_cmd(
    ["afk"],
    propagate_to_next_handler=False,
    cmd_help={
        "help": "Set AFK!",
        "example": "{ch}afk Tidur",
    },
)
async def afk_set(client, message):
    global AFK_REASON, AFK, AFK_TIME

    cmd = message.command
    afk_text = ""

    if len(cmd) > 1:
        afk_text = " ".join(cmd[1:])

    if isinstance(afk_text, str):
        AFK_REASON = afk_text

    AFK = True
    AFK_TIME = datetime.now()

    await message.delete()


@Panda_cmd(
    ["afk"],
    propagate_to_next_handler=False,
    cmd_help={
        "help": "Set AFK!",
        "example": "{ch}afk Tidur",
    },
)
async def afk_unset(client, message):
    global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
        await message.edit(
            f"`While you were away (for {last_seen}), you received {sum(USERS.values()) + sum(GROUPS.values())} "
            f"messages from {len(USERS) + len(GROUPS)} chats`"
        )
        AFK = False
        AFK_TIME = ""
        AFK_REASON = ""
        USERS = {}
        GROUPS = {}
        await asyncio.sleep(5)

    await message.delete()


@listen(filters.outgoing & filters.me)
async def auto_afk_unset(client, message):
    global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
        reply = await message.reply(
            f"`While you were away (for {last_seen}), you received {sum(USERS.values()) + sum(GROUPS.values())} "
            f"messages from {len(USERS) + len(GROUPS)} chats`"
        )
        AFK = False
        AFK_TIME = ""
        AFK_REASON = ""
        USERS = {}
        GROUPS = {}
        await asyncio.sleep(5)
        await reply.delete()
