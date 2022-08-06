import random
from Panda.events import pyroregister
import asyncio
from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import (
    edit_or_reply,
    edit_or_send_as_file,
    get_text,
    get_user,
    is_admin_or_owner,
)
from pyrogram import filters

pengguna = [
    f"Perkenalkan Nama saya Panda\nTerimah Kasih Ganteng 😏",
    f"Saya Panda Hadir Kang mas ucok butet neng atau apalah 😂😏",
    f"Terimakasih buat owner Yang ganteng 😊",
    f"Kamshamida owner ganteng 😂 ",
    f"✅ Panda Aktif  ✅",
]

DEV = [5061420797, 1593802955, 5057493677, 1338398753, 1743866353]
        
@ilhammansiz_on_cmd(
    ["absen"],
    cmd_help={
        "help": "Absen",
        "example": "{ch}absen",
    },
)
async def absen(client, message): 
    salam = await message.reply(random.choice(pengguna))
    await asyncio.sleep(10)
    await salam.delete()
    
