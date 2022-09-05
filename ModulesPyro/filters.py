from pyrogram import filters

from Panda.database.filterdb import (
    add_filters,
    all_filters,
    del_filters,
    filters_del,
    filters_info,
)
from Panda import Config
from Panda._func.decorators import Panda_cmd, listen
from Panda._func._helpers import edit_or_reply, get_text
from . import HELP

HELP(
    "filters",
)

@Panda_cmd(
    ["delfilter"],
    cmd_help={"help": "Delete A Filter!", "example": "{ch}delfilter (filter name)"},
)
async def del_filterz(client, message):
    note_ = await edit_or_reply(message, "`Processing..`")
    note_name = get_text(message)
    if not note_name:
        await note_.edit("`Give A Filter Name!`")
        return
    note_name = note_name.lower()
    if not filters_info(note_name, message.chat.id):
        await note_.edit("`Filter Not Found!`")
        return
    del_filters(note_name, message.chat.id)
    await note_.edit(f"`Filter {note_name} Deleted Successfully!`")


@Panda_cmd(
    ["filters"],
    cmd_help={"help": "List All The Filters In The Chat!", "example": "{ch}filters"},
)
async def show_filters(client, message):
    pablo = await edit_or_reply(message, "`Processing..`")
    poppy = all_filters(message.chat.id)
    if poppy is False:
        await pablo.edit("`No Filters Found In This Chat...`")
        return
    kk = ""
    for Escobar in poppy:
        kk += f"\n > `{Escobar.get('keyword')}`"
    X = await client.get_chat(message.chat.id)
    grp_nme = X.title
    mag = f"List Of Filters In {grp_nme}: \n{kk}"
    await pablo.edit(mag)


@Panda_cmd(
    ["savefilter"],
    cmd_help={
        "help": "Save A Filter!",
        "example": "{ch}savefilter (filter name) (replying to message)",
    },
)
async def s_filters(client, message):
    note_ = await edit_or_reply(message, "`Processing..`")
    note_name = get_text(message)
    if not note_name:
        await note_.edit("`Give A Filter Name!`")
        return
    if not message.reply_to_message:
        await note_.edit("Reply To Message To Save As Filter!")
        return
    note_name = note_name.lower()
    msg = message.reply_to_message
    copied_msg = await msg.copy(Config.LOG_GRP)
    add_filters(note_name, message.chat.id, copied_msg.message_id)
    await note_.edit(f"`Done! {note_name} Added To Filters List!`")


@listen(filters.incoming & ~filters.edited & filters.group)
async def filter_s(client, message):
    if all_filters(message.chat.id):
        pass
    else:
        message.continue_propagation()
    owo = message.text
    if owo is None:
        message.continue_propagation()
    owoo = owo.lower()
    tges = owoo.split(" ")
    for owo in tges:
        if filters_info(owo, message.chat.id):
            sed = filters_info(owo, message.chat.id)
            await client.copy_message(
                from_chat_id=Config.LOG_GRP,
                chat_id=message.chat.id,
                message_id=sed["msg_id"],
                reply_to_message_id=message.message_id,
            )
    message.continue_propagation()


@Panda_cmd(
    ["delfilters"],
    cmd_help={"help": "Delete All The Filters in chat!", "example": "{ch}delfilters"},
)
async def del_all_filters(client, message):
    pablo = await edit_or_reply(message, "`Processing...`")
    poppy = all_filters(message.chat.id)
    if poppy is False:
        await pablo.edit("`No Filters Found In This Chat...`")
        return
    filters_del(message.chat.id)
    await pablo.edit("Deleted All The Filters Successfully!!")
