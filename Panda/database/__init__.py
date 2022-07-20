import motor.motor_asyncio
from ..Var import Database


def mongodb():
    if Database.MONGO_DB:
        return motor.motor_asyncio.AsyncIOMotorClient(Database.MONGO_DB)
    else:
        return None


db_x = mongodb()


