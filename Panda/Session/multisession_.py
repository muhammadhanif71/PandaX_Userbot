
from .pyroclient import pyrotgbot

def Pyrogram():
    if pyrotgbot:
        pyrotgbot.start()
        pyrotgbot.me = await pyrotgbot.get_me()
   
    if pyrobot:
       pyrobot.start()
       pyrobot.me = await pyrobot.get_me()
