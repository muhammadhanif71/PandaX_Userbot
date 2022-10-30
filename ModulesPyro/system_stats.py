import platform
import re
import socket
import sys
import time
import uuid
from datetime import datetime
from os import environ, execle
import random
import psutil
from pyrogram import __version__

from Panda import Config, pandaversion, StartTime as start_time, DB
from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import (
    delete_or_pass,
    edit_or_reply,
    get_readable_time,
    humanbytes,
)

from . import HELP

custom_text = " 𝐏𝐚𝐧𝐝𝐚 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐁𝐎𝐓_𝐈𝐒_𝐑𝐔𝐍𝐍𝐈𝐍𝐆 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐏𝐚𝐧𝐝𝐚_𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐀𝐜𝐭𝐢𝐯𝐞".split(
    " "
)

emoji_alive = "★ ♦ ♠ ♣ ¡ ! ‹ › ∞ ≈ × 🦌 🐘 🐨 🐼 🐧 🦇 🦃 🐲 💮 🌸 🌺 🌻 🌼 🏵 🌳 🌲 🌺 🎭 🌟 🌠 🌩 ⚡ 🔥 ☄️ ❄ 🛸 ✨ 🎑 ⚒️ 🛠 ⛏️ 🔨 ⚔️ 🗡 ⚙️ 🏹 🔮 🗿 ⚱️ ⚰️ ➡️ ↗️ ⬆️ ⬅️ ↘️ ⬇️ ✅ ☑️ ❓ ⁉️ ‼️ ❗🇲🇨 🇹🇷 🇩🇪".split(
    " "
)


HELP(
    "system_stats",
)

@ilhammansiz_on_cmd(
    ["ping", "pong"],
    cmd_help={"help": "Check Bot Uptime!", "example": "{ch}ping"},
)
async def pingy(client, message):
    start = datetime.now()
    hmm = await edit_or_reply(message, "`Pong!`")
    uptime = get_readable_time((time.time() - start_time))
    myself = client.me
    if not myself.username:
        myself.id
    else:
        f"@{myself.username}"
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"**┏━《 **★𝗣 𝗔 𝗡 𝗗 𝗔★** 》━\n**┣➠  __Ping:__** `{ms}` \n┗➠ __Uptime:__ `{uptime}`",
    )


@ilhammansiz_on_cmd(
    ["alive"],
    cmd_help={"help": "Get Alive Message Of Your Bot.!", "example": "{ch}alive"},
)
async def amialive(client, message):
    img_ = Config.ALIVE_IMG
    me_ = client.me.first_name
    du = psutil.disk_usage(client.workdir)
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    alive = f"""
{random.choice(custom_text)}
 {random.choice(emoji_alive)}**Name: {me_}**
 {random.choice(emoji_alive)}**Version :** `{pandaversion}`
 {random.choice(emoji_alive)}**Uptime :** __{get_readable_time((time.time() - start_time))}__
 {random.choice(emoji_alive)}**Pyrogram Version :** __{__version__}__
 {random.choice(emoji_alive)}**Python Version :** __{platform.python_version()}__
 {random.choice(emoji_alive)}**OS :** __{platform.system()}__
 {random.choice(emoji_alive)}**CPU :** __{len(psutil.Process().cpu_affinity())}__
 {random.choice(emoji_alive)}**DISK USAGE :** __{disk}__
 {random.choice(emoji_alive)}**Database :** {DB.name} {DB.ping()}
"""
    if message.reply_to_message:
        await client.send_photo(
            message.chat.id,
            img_,
            caption=alive,
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_photo(message.chat.id, img_, caption=alive)
    await delete_or_pass(message)


@ilhammansiz_on_cmd(
    ["sysinfo", "neofetch"],
    cmd_help={"help": "Get System Information!", "example": "{ch}sysinfo"},
)
async def give_sysinfo(client, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    neat_msg = f"""**System Info**
    
**PlatForm :** `{splatform}`
**PlatForm - Release :** `{platform_release}`
**PlatFork - Version :** `{platform_version}`
**Architecture :** `{architecture}`
**Hostname :** `{hostname}`
**IP :** `{ip_address}`
**Mac :** `{mac_address}`
**Processor :** `{processor}`
**Ram : ** `{ram}`
**CPU :** `{cpu_len}`
**CPU FREQ :** `{cpu_freq}`
**DISK :** `{disk}`
    """
    await edit_or_reply(message, neat_msg)


@ilhammansiz_on_cmd(
    ["restart"],
    cmd_help={"help": "Restart Your Bot!", "example": "{ch}restart"},
)
async def wow_restart(client, message):
    await edit_or_reply(message, "`Restarting...`")
    args = [sys.executable, "-m", "userbot"]
    execle(sys.executable, *args, environ)
    exit()
    return
