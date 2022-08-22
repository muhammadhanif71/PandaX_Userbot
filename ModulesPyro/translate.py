
from gpytranslate import Translator

from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import (
    edit_or_reply, 
    get_text,
)

from . import HELP


HELP(
    "translate",
)

"""
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

"""

from asyncio import sleep

from googletrans import LANGUAGES, Translator
from Panda.sql_helper.globals import addgvar, gvarstatus
from Panda import BOTLOG, BOTLOG_CHATID



# https://github.com/ssut/py-googletrans/issues/234#issuecomment-722379788
async def getTranslate(text, **kwargs):
    translator = Translator()
    result = None
    for _ in range(10):
        try:
            result = translator.translate(text, **kwargs)
        except Exception:
            translator = Translator()
            await sleep(0.1)
    return result



@ilhammansiz_on_cmd(
    ["tl"],
    cmd_help={
        "help": "Translate!",
        "example": "{ch}tl <language code> ; <text>",
    },
)
async def translate(client, message):
    "To translate the text."
    input_str = get_text(message)
    if message.reply_to_message:
        previous_message = message.reply_to_message.text
        text = previous_message.message
        lan = input_str or "id"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        return await edit_delete(
            message, "`.tl LanguageCode` as reply to a message", time=5
        )
    text = text.strip()
    lan = lan.strip()
    Translator()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"**TRANSLATED from {LANGUAGES[translated.src].title()} to {LANGUAGES[lan].title()}**\
                \n`{after_tr_text}`"
        await edit_or_reply(message, output_str)
    except Exception as exc:
        await edit_delete(message, f"**Error:**\n`{str(exc)}`", time=5)


@ilhammansiz_on_cmd(
    ["tr"],
    cmd_help={
        "help": "Translate!",
        "example": "{ch}tr <text>",
    },
)
async def translateme(client, message):
    "To translate the text to required language."
    textx = message.reply_to_message.text
    message = get_text(message)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await edit_or_reply(
            trans, "`Give a text or reply to a message to translate!`"
        )
    TRT_LANG = gvarstatus("TRT_LANG") or "id"
    try:
        reply_text = await getTranslate(message, dest=TRT_LANG)
    except ValueError:
        return await edit_delete(message, "`Invalid destination language.`", time=5)
    source_lan = LANGUAGES[f"{reply_text.src.lower()}"]
    transl_lan = LANGUAGES[f"{reply_text.dest.lower()}"]
    reply_text = f"**From {source_lan.title()}({reply_text.src.lower()}) to {transl_lan.title()}({reply_text.dest.lower()}) :**\n`{reply_text.text}`"

    await edit_or_reply(message, reply_text)
    if BOTLOG:
        await client.send_message(
            BOTLOG_CHATID,
            f"`Translated some {source_lan.title()} stuff to {transl_lan.title()} just now.`",
        )



@ilhammansiz_on_cmd(
    ["lang"],
    cmd_help={
        "help": "default language for trt command",
        "example": "{ch}lang trt id",
    },
)
async def lang(client, message):
    "To set language for trt comamnd."
    arg = get_text(message)
    input_str = get_text(message)
    if arg not in LANGUAGES:
        return await edit_or_reply(
            message,
            f"`Invalid Language code !!`\n`Available language codes for TRT`:\n\n`{LANGUAGES}`",
        )
    LANG = LANGUAGES[arg]
    if input_str == "trt":
        addgvar("TRT_LANG", arg)
        await edit_or_reply(
            message, f"`Language for Translator changed to {LANG.title()}.`"
        )
    else:
        addgvar("AI_LANG", arg)
        await edit_or_reply(
            message, f"`Language for chatbot is changed to {LANG.title()}.`"
        )
    LANG = LANGUAGES[arg]

    if BOTLOG:
        if input_str == "trt":
            await client.send_message(
                BOTLOG_CHATID, f"`Language for Translator changed to {LANG.title()}.`"
            )
        if input_str == "ai":
            await client.send_message(
                BOTLOG_CHATID, f"`Language for chatbot is changed to {LANG.title()}.`"
            )

