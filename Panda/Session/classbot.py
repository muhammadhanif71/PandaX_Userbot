from pyrogram import Client
import os
PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or "-1001718757023")

from ..Var import Database

class Pyrobot(Client):
    def __init__(self):
        super().__init__(
            "BotToken",
            api_id=Database.APP_ID,
            api_hash=Database.API_HASH,
            bot_token=Database.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                PRIVATE_GROUP_BOT_API_ID, "Starting Bot"
            )
        except:
            await self.send_message(
                PRIVATE_GROUP_BOT_API_ID, "Bot has failed to access the log Group."
            )
            sys.exit()
