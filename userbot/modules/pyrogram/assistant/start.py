from pyrogram import filters
from pyrogram.types import Message

from .... import app


@app.bot.on_message(filters.command("start"))
async def send_response(_, m: Message):
    await m.reply("How can i help You ?")


@app.bot.on_message(filters.new_chat_members & filters.group)
async def added_to_group_msg(_, m: Message):
    if m.new_chat_members[0].is_self:
        try:
            await app.bot.send_message(
                m.chat.id,
                "Thank You for adding me in this group !\nUse /help to know my features.",
            )
        except Exception as e:
            await app.error(m, e)
    else:
        return
