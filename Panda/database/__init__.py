import motor.motor_asyncio
from ..Var import Database
import logging
from ..sql_helper.db import BaseDB
"""
def mongodb():
    if Database.MONGO_DB:
        return motor.motor_asyncio.AsyncIOMotorClient(Database.MONGO_DB)
    else:
        return None


db_x = mongodb()

"""


db_x = BaseDB()
