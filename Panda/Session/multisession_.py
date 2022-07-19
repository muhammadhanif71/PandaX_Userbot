
from .pyroclient import pyrobot, pyrobot2, pyrobot3, pyrobot4, pyrotgbot

def Pyrogram():
    if pyrotgbot:
        await pyrotgbot.start()
        pyrotgbot.me = await pyrotgbot.get_me()
   
