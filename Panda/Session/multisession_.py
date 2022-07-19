
from .pyroclient import pyrotgbot

def Pyrogram():
    if pyrotgbot:
        await pyrotgbot.start()
        pyrotgbot.me = await pyrotgbot.get_me()
   
