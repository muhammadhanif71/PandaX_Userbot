
from .pyroclient import pyrotgbot, pyrobot

def Pyrogram():
    if pyrotgbot:
        pyrotgbot.start()
        pyrotgbot.me = pyrotgbot.get_me()
   
    if pyrobot:
       pyrobot.start()
       pyrobot.me = pyrobot.get_me()
