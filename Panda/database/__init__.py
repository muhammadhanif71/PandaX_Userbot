import motor.motor_asyncio
from ..Var import Database
import logging
"""
def mongodb():
    if Database.MONGO_DB:
        return motor.motor_asyncio.AsyncIOMotorClient(Database.MONGO_DB)
    else:
        return None


db_x = mongodb()

"""

__all__ = ['get_collection']

import asyncio
from typing import List

from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection

from . import logbot

_LOG = logging.getLogger(__name__)
_LOG_STR = "$$$>>> %s <<<$$$"

logbot.edit_last_msg("Connecting to Database ...", _LOG.info, _LOG_STR)

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(Database.MONGO_DB)
_RUN = asyncio.get_event_loop().run_until_complete

if "Panda" in _RUN(_MGCLIENT.list_database_names()):
    _LOG.info(_LOG_STR, "Panda Database Found :) => Now Logging to it...")
else:
    _LOG.info(_LOG_STR, "Panda Database Not Found :( => Creating New Database...")

_DATABASE: AgnosticDatabase = _MGCLIENT["Panda"]
_COL_LIST: List[str] = _RUN(_DATABASE.list_collection_names())


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    if name in _COL_LIST:
        _LOG.debug(_LOG_STR, f"{name} Collection Found :) => Now Logging to it...")
    else:
        _LOG.debug(_LOG_STR, f"{name} Collection Not Found :( => Creating New Collection...")
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()


logbot.del_last_msg()


def mongodb():
    if Database.MONGO_DB:
        return get_collection
    else:
        return None


db_x = mongodb()
