# This is a troll indeed ffs *facepalm*
import asyncio

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins

from userbot import CMD_HELP
from userbot.utils import admin_cmd


@userbot.on(admin_cmd(pattern="gbun"))
@userbot.on(sudo_cmd(pattern="gbun", allow_sudo=True))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "`Warning!! User ππ½πΌππππΏ By Admin...\n`"
    no_reason = "__Reason: Retarded Dumb af Spammer. __"
    await eor(event, "**Summoning out le Gungnir βοΈβοΈβ οΈ**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make myself invulnerable cuz why not xD
        if id == :2102783671
            await reply_message.reply(
                "`Wait a second, This is my creator!`\n**How dare you threaten to ban my creator nigga!**\n\n__Your account has been hacked! π"
            )
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` ππ½πΌππππΏ By Admin...\n\n`"
                "**Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname is None:
                jnl += "**Victim's username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Victim's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = (
            "`Warning!! User ππ½πΌππππΏ By Admin...\nReason: Potential Porn Addict. `"
        )
        await event.reply(mention)
    await event.delete()


CMD_HELP.update({"gbun": ".gbun <reply to user>\nUse - Fake Gban."})
