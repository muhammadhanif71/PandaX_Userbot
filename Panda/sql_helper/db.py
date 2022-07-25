# Copyright (C) 2021-2022 TeamUltroid
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

# Recode by @robotrakitangakbagus, @diemmmmmmmmmm
# Import PandaX_Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# t.me/PandaUserbot & t.me/TeamSquadUserbotSupport


import sys

from Panda.Var import Var
from Panda.core.logger import logging

LOGS = logging.getLogger("PandaUserbot")

try:
    from pymongo import MongoClient
except ImportError:
    MongoClient = None
    if Var.MONGO_URI:
        LOGS.warning(
            "'pymongo' not found!\nInstall pymongo[srv] to use Mongo database.."
        )

try:
    import psycopg2
except ImportError:
    psycopg2 = None
    if Var.DB_URI:
        LOGS.warning("'psycopg2' not found!\nInstall psycopg2 to use SQL database..")


class MongoDB:
    def __init__(self, key):
        self.dB = MongoClient(key, serverSelectionTimeoutMS=5000)
        self.db = self.dB.BaseDB
        self.re_cache()

    def __repr__(self):
        return f"<Base.MonGoDB\n -total_keys: {len(self.keys())}\n>"

    @property
    def name(self):
        return "Mongo"

    @property
    def usage(self):
        return self.db.command("dbstats")["dataSize"]

    def re_cache(self):
        self._cache = {}
        for key in self.keys():
            self._cache.update({key: self.get_key(key)})

    def ping(self):
        if self.dB.server_info():
            return True

    def keys(self):
        return self.db.list_collection_names()

    def setdb(self, key, value):
        if key in self.keys():
            self.db[key].replace_one({"_id": key}, {"value": str(value)})
        else:
            self.db[key].insert_one({"_id": key, "value": str(value)})
        self._cache.update({key: value})
        return True

    def deldb(self, key):
        if key in self.keys():
            try:
                del self._cache[key]
            except KeyError:
                pass
            self.db.drop_collection(key)
            return True

    def getdb(self, key):
        if key in self._cache:
            return self._cache[key]
        if key in self.keys():
            value = get_data(self, key)
            self._cache.update({key: value})
            return value
        return None

    def get(self, key):
        if x := self.db[key].find_one({"_id": key}):
            return x["value"]

    def flushall(self):
        self.dB.drop_database("BaseDB")
        self._cache = {}
        return True


# --------------------------------------------------------------------------------------------- #

# Thanks to "Akash Pattnaik" / @BLUE-DEVIL1134
# for SQL Implementation in Ultroid.
#
# Please use https://elephantsql.com/ !


class SqlDB:
    def __init__(self, url):
        self._url = url
        self._connection = None
        self._cursor = None
        try:
            self._connection = psycopg2.connect(dsn=url)
            self._connection.autocommit = True
            self._cursor = self._connection.cursor()
            self._cursor.execute(
                "CREATE TABLE IF NOT EXISTS PandaUserbot)"
            )
        except Exception as error:
            LOGS.exception(error)
            LOGS.info("Invaid SQL Database")
            if self._connection:
                self._connection.close()
            sys.exit()
        self.re_cache()

    @property
    def name(self):
        return "SQL"

    @property
    def usage(self):
        self._cursor.execute(
            "SELECT pg_size_pretty(pg_relation_size('PandaUserbot')) AS size"
        )
        data = self._cursor.fetchall()
        return int(data[0][0].split()[0])

    def re_cache(self):
        self._cache = {}
        for key in self.keys():
            self._cache.update({key: self.get_key(key)})

    def keys(self):
        self._cursor.execute(
            "SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name  = 'panda'"
        )  # case sensitive
        data = self._cursor.fetchall()
        return [_[0] for _ in data]

    def ping(self):
        return True

    def getdb(self, variable):
        if variable in self._cache:
            return self._cache[variable]
        get_ = get_data(self, variable)
        self._cache.update({variable: get_})
        return get_

    def get(self, variable):
        try:
            self._cursor.execute(f"SELECT {variable} FROM Panda")
        except psycopg2.errors.UndefinedColumn:
            return None
        data = self._cursor.fetchall()
        if not data:
            return None
        if len(data) >= 1:
            for i in data:
                if i[0]:
                    return i[0]

    def setdb(self, key, value):
        try:
            self._cursor.execute(f"ALTER TABLE Panda DROP COLUMN IF EXISTS {key}")
        except (psycopg2.errors.UndefinedColumn, psycopg2.errors.SyntaxError):
            pass
        except BaseException as er:
            LOGS.exception(er)
        self._cache.update({key: value})
        self._cursor.execute(f"ALTER TABLE Panda ADD {key} TEXT")
        self._cursor.execute(f"INSERT INTO Panda ({key}) values (%s)", (str(value),))
        return True

    def deldb(self, key):
        if key in self._cache:
            del self._cache[key]
        try:
            self._cursor.execute(f"ALTER TABLE Ultroid DROP COLUMN {key}")
        except psycopg2.errors.UndefinedColumn:
            return False
        return True

    delete = deldb

    def flushall(self):
        self._cache.clear()
        self._cursor.execute("DROP TABLE PandaUserbot")
        self._cursor.execute(
            "CREATE TABLE IF NOT EXISTS PandaUserbot)"
        )
        return True

    def rename(self, key1, key2):
        _ = self.get_key(key1)
        if _:
            self.del_key(key1)
            self.set_key(key2, _)
            return 0
        return 1


# --------------------------------------------------------------------------------------------- #





def BaseDB():
    if MongoClient and Var.MONGO_URI:
        return MongoDB(Var.MONGO_URI)
    else:
        return None

    if psycopg2 and Var.DB_URI:
        return SqlDB(Var.DB_URI)
    else:
        return None
    
 
