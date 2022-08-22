from pyrogram.raw.functions.account import UpdateProfile as UpdateProfileRequest
from pyrogram.raw.functions.photos import DeletePhotos, UploadProfilePhoto
from pyrogram.raw.functions.users import GetFullUser as GetFullUserRequest
from pyrogram.raw.types import InputPhoto

DeletePhotosRequest = DeletePhotos
UploadProfilePhotoRequest = UploadProfilePhoto

from Panda import DEVLIST as DEVS, LOGS, STORAGE, pyrobot
from Panda._func.decorators import Panda_cmd as ilhammansiz_on_cmd
from Panda._func._helpers import edit_or_reply, get_text, get_user

if not hasattr(STORAGE, "userObj"):
    STORAGE.userObj = False


@ilhammansiz_on_cmd(
    ["clone"],
    cmd_help={
        "help": "Absen",
        "example": "{ch}clone username/reply to user",
    },
)
async def impostor(client, message):
    inputArgs = get_text(message)
    xx = await edit_or_reply(message, "`Processing...`")
    if "restore" in inputArgs:
        await message.edit("**Kembali ke identitas asli...**")
        if not STORAGE.userObj:
            return await xx.edit("**Anda harus mengclone orang dulu sebelum kembali!**")
        await updateProfile(client, STORAGE.userObj, restore=True)
        return await xx.edit("**Berhasil Mengembalikan Akun Anda dari clone**")
    if inputArgs:
        try:
            userk = get_user(message, inputArgs)[0]
            user = await pyrobot.get_users(userk)
        except BaseException:
            return await xx.edit("**Username/ID tidak valid.**")
        userObj = await pyrobot(GetFullUserRequest(user))
    elif message.reply_to_message:
        replyMessage = message.reply_to_message.text
        if replyMessage.sender_id in DEVS:
            return await xx.edit(
                "**Tidak dapat menyamar sebagai developer PandaUserbot 😡**"
            )
        if replyMessage.sender_id is None:
            return await xx.edit("**Tidak dapat menyamar sebagai admin anonim 🥺**")
        userObj = await pyrobot(GetFullUserRequest(replyMessage.sender_id))
    else:
        return await xx.edit("**Ketik** `.help clone` **bila butuh bantuan.**")

    if not STORAGE.userObj:
        STORAGE.userObj = await pyrobot(GetFullUserRequest(message.sender_id))

    LOGS.info(STORAGE.userObj)
    await xx.edit("**Mencuri identitas orang ini...**")
    await updateProfile(client, userObj)
    await xx.edit("**Aku adalah kamu dan kamu adalah aku. asekk 🥴**")


async def updateProfile(client, userObj, restore=False):
    firstName = (
        "Deleted Account"
        if userObj.user.first_name is None
        else userObj.user.first_name
    )
    lastName = "" if userObj.user.last_name is None else userObj.user.last_name
    userAbout = userObj.about if userObj.about is not None else ""
    userAbout = "" if len(userAbout) > 70 else userAbout
    if restore:
        userPfps = await pyrobot.get_profile_photos("me")
        userPfp = userPfps[0]
        await pyrobot(
            DeletePhotosRequest(
                id=[
                    InputPhoto(
                        id=userPfp.id,
                        access_hash=userPfp.access_hash,
                        file_reference=userPfp.file_reference,
                    )
                ]
            )
        )
    else:
        try:
            userPfp = userObj.profile_photo
            pfpImage = await pyrobot.download_media(userPfp)
            await pyrobot(
                UploadProfilePhotoRequest(await client.upload_file(pfpImage))
            )
        except BaseException:
            pass
    await pyrobot(
        UpdateProfileRequest(about=userAbout, first_name=firstName, last_name=lastName)
    )
