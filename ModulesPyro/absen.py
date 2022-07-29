import random
from Panda.events import pyroregister
from pyrogram import Client, filters


pengguna = [
    f"Perkenalkan Nama saya Panda\nTerimah Kasih Ganteng 😏",
    f"Saya Panda Hadir Kang mas ucok butet neng atau apalah 😂😏",
    f"Terimakasih buat owner Yang ganteng 😊",
    f"Kamshamida owner ganteng 😂 ",
    f"✅ Panda Aktif  ✅",
]

DEV = [5061420797, 1593802955, 5057493677, 1338398753, 1743866353]
        
@pyroregister(filters.user(DEV), pattern=r"^absen$")
async def _(event): 
    salam = await event.reply(random.choice(pengguna))
    await asyncio.sleep(10)
    await salam.delete()
    
