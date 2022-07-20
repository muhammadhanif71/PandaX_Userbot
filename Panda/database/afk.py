from .. import SqL


afk = SqL


async def go_afk(time, reason=""):
    midhun = afk.getdb({"_id": "AFK"})
    if midhun:
        await afk.setdb({"_id": "AFK"}, {"$set": {"time": time, "reason": reason}})
    else:
        await afk.setdb({"_id": "AFK", "time": time, "reason": reason})


async def no_afk():
    midhun = afk.getdb({"_id": "AFK"})
    if midhun:
        afk.deldb({"_id": "AFK"})


async def check_afk():
    midhun = afk.getdb({"_id": "AFK"})
    if midhun:
        return midhun
    else:
        return None
