from datetime import datetime
from Panda import pyrobot
# noinspection PyPackageRequirements
from pyrogram import emoji, filters
from pyrogram.types import Message
from pyrogram.utils import MAX_CHANNEL_ID
from pytgcalls import GroupCallFactory, GroupCallFileAction

DELETE_DELAY = 8
DURATION_AUTOPLAY_MIN = 10
DURATION_PLAY_HOUR = 3


main_filter = (filters.group
               & filters.text
               & ~filters.edited
               & ~filters.via_bot)
self_or_contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


async def current_vc_filter(_, __, m: Message):
    group_call = mp.group_call
    if not (group_call and group_call.is_connected):
        return False
    chat_id = int("-100" + str(group_call.full_chat.id))
    if m.chat.id == chat_id:
        return True
    return False


current_vc = filters.create(current_vc_filter)


class MusicPlayer(object):
    def __init__(self):
        self.group_call = None
        self.client = None
        self.chat_id = None
        self.start_time = None
        self.playlist = []
        self.msg = {}

    async def update_start_time(self, reset=False):
        self.start_time = (
            None if reset
            else datetime.utcnow().replace(microsecond=0)
        )

    async def send_playlist(self):
        playlist = self.playlist
        if not playlist:
            pl = f"{emoji.NO_ENTRY} empty playlist"
        else:
            if len(playlist) == 1:
                pl = f"{emoji.REPEAT_SINGLE_BUTTON} **Playlist**:\n"
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n"
            pl += "\n".join([
                f"**{i}**. **[{x.audio.title}]({x.link})**"
                for i, x in enumerate(playlist)
            ])
        if mp.msg.get('playlist') is not None:
            await mp.msg['playlist'].delete()
        mp.msg['playlist'] = await send_text(pl)


mp = MusicPlayer()


# - pytgcalls handlers


async def network_status_changed_handler(context, is_connected: bool):
    if is_connected:
        mp.chat_id = MAX_CHANNEL_ID - context.full_chat.id
        await send_text(f"{emoji.CHECK_MARK_BUTTON} joined the voice chat")
    else:
        await send_text(f"{emoji.CROSS_MARK_BUTTON} left the voice chat")
        mp.chat_id = None


async def playout_ended_handler(_, __):
    await skip_current_playing()






@pyrobot.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("^.joinvc$"))
async def join_group_call(client, m: Message):
    group_call = mp.group_call
    if not group_call:
        mp.group_call = GroupCallFactory(client).get_file_group_call()
        mp.group_call.add_handler(network_status_changed_handler,
                                  GroupCallFileAction.NETWORK_STATUS_CHANGED)
        mp.group_call.add_handler(playout_ended_handler,
                                  GroupCallFileAction.PLAYOUT_ENDED)
        await mp.group_call.start(m.chat.id)
        await m.delete()
    if group_call and group_call.is_connected:
        await m.reply_text(f"{emoji.ROBOT} already joined a voice chat")


@pyrobot.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^.leavevc$"))
async def leave_voice_chat(_, m: Message):
    group_call = mp.group_call
    mp.playlist.clear()
    group_call.input_filename = ''
    await group_call.stop()
    await m.delete()
