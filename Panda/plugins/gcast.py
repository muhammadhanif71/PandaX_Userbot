# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
# Recode by Ilham Mansiez

import asyncio
import base64
from telethon.errors.rpcerrorlist import FloodWaitError

from Panda import PandaBot
import Panda
plugin_category = "plugins"




@PandaBot.ilhammansiz_cmd(
    pattern="en(?: |$)(.*)",
    command=("encode", plugin_category),
    info={
        "header": "encode ",
        "usage": "{tr}en text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Encode..`")
    byt = ppk.encode("ascii")
    et = base64.b64encode(byt)
    atc = et.decode("ascii")
    await edit_or_reply(event,
        f"**=>> Encoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
    )

@PandaBot.ilhammansiz_cmd(
    pattern="de(?: |$)(.*)",
    command=("decode", plugin_category),
    info={
        "header": "decode ",
        "usage": "{tr}de text",
    },
)
async def encode(event):
    ppk = event.pattern_match.group(1)
    event.chat.id
    if not ppk:
        return await edit_or_reply(event, "`Give me Something to Decode..`")
    byt = ppk.encode("ascii")
    try:
        et = base64.b64decode(byt)
        atc = et.decode("ascii")
        await edit_or_reply(event,
            f"**=>> Decoded Text :** `{ppk}`\n\n**=>> OUTPUT :**\n`{atc}`"
        )
    except Exception as p:
        await edit_or_reply(event, "**ERROR :** " + str(p))



@PandaBot.ilhammansiz_cmd(
    pattern="gcast(?: |$)(.*)",
    command=("gcast", plugin_category),
    info={
        "header": "Promosi kesemua grup yang dimasuki ",
        "usage": "{tr}gcast text/media",
    },
)
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Saya Text Untuk Di Broadcast**")
    kk = await edit_or_reply(event, "`• 📢 Global Broadcast Di Prosess Cok...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in Panda.Gblacklist:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**╭✠╼━━━━━━❖━━━━━━━✠╮** Broadcast Terkirim Ke =** `{done}` **Grup, Broadcast Gagal Terkirim =** `{er}`**Grup**╰✠╼━━━━━━❖━━━━━━━✠╯**"
    )





@PandaBot.ilhammansiz_cmd(
    pattern="gucast(?: |$)(.*)",
    command=("gucast", plugin_category),
    info={
        "header": "Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)",
        "usage": "{tr}gucast text/media",
    },
)
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Globally Broadcasting processing...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in Panda.DEVLIST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**╭✠╼━━━━━━❖━━━━━━━✠╮** Broadcast Terkirim Ke =** `{done}` **chat, Gagal Mengirim Pesan Ke = `{er}`**╰✠╼━━━━━━❖━━━━━━━✠╯"
    )
