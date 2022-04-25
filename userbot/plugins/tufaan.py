import time

from userbot import StartTime, tufaanversion
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon import events, version
from userbot.exampleconfig import Config
from . import *

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "TUFAAN USER"
TUFAAN_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or " #ɬųʄąąŋ_ơŋ_ʄıཞɛ 🔥⚡"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="tufaan$"))
@bot.on(sudo_cmd(pattern="tufaan$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if TUFAAN_IMG:
        tufaan_caption = f"**🔥 TυϝααɳBσƚ Iʂ Oɳʅιɳҽ 🔥**\n\n"
        
        tufaan_caption += f"**✘ 𝗠𝗮𝘀𝘁𝗲𝗿 : **{mention}\n\n\n"
        tufaan_caption += f"**✘ 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 :** `{version.__version__}`\n"
        tufaan_caption += f"**✘ 𝗧𝘂𝗳𝗮𝗮𝗻 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 :** `{tufaanversion}`\n"
        tufaan_caption += f"**✘ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹:** `[TufaanBot](https://t.me/TheTufaanBot)\n`"
        tufaan_caption += f"**✘ 𝗖𝗿𝗲𝗮𝘁𝗼𝗿 :** [Akhil](https://t.meAkHiL_SI)\n",
        tufaan_caption += f"** _[🔗 TUFAANBOT SOURCE 🔥](https://GitHub.com/AKHIL-SI/TheTufaanBot)\n

        await alive.client.send_file(
            alive.chat_id, TUFAAN_IMG, caption=TUFAAN_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**🔥 TυϝααɳBσƚ Iʂ Oɳʅιɳҽ 🔥 **\n\n"
            
            f"**✘ 𝗠𝗮𝘀𝘁𝗲𝗿 : **{mention}\n\n"
            f"**✘ 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 :** `{version.__version__}`\n"
            f"**✘ 𝗧𝘂𝗳𝗮𝗮𝗻 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 :** `{tufaanversion}`\n"
            f"**✘ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹:** `[TufaanBot](https://t.me/TheTufaanBot)\n`"
            f"**✘ 𝗖𝗿𝗲𝗮𝘁𝗼𝗿 :** [Akhil](https://t.meAkHiL_SI)\n",
            f"** _[🔗 TUFAANBOT SOURCE 🔥](https://github.com/AKHIL-SI/TheTufaanBot)\n
)
