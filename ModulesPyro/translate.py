
from gpytranslate import Translator
from pyrogram import Client, filters
from pyrogram.types import Message

from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd, listen
from Panda._func._helpers import (
    edit_or_reply,
    edit_or_send_as_file,
    get_text,
    get_user,
    iter_chats,
)


@ilhammansiz_on_cmd(
    ["tr"],
    cmd_help={
        "help": "Translate!",
        "example": "{ch}tr id (reply to user messages OR provide his word)",
    },
)
async def translate(client, message):
    trl = Translator()
    if message.reply_to_message and (
        message.reply_to_message.text or message.reply_to_message.caption
    ):
        input_str = (
            message.text.split(None, 1)[1]
            if len(
                message.command,
            )
            != 1
            else None
        )
        target = input_str or "id"
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await edit_or_reply(
                message, f"**ERROR:** `{str(err)}`", parse_mode="Markdown"
            )
            return
    else:
        input_str = (
            message.text.split(None, 2)[1]
            if len(
                message.command,
            )
            != 1
            else None
        )
        text = message.text.split(None, 2)[2]
        target = input_str or "id"
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await edit_or_reply(
                message, "**ERROR:** `{}`".format(str(err)), parse_mode="Markdown"
            )
            return
    await edit_or_reply(
        message,
        f"**Translated:**\n```{tekstr.text}```\n\n**Detected Language:** `{(await trl.detect(text))}`",
        parse_mode="Markdown",
    )


