import asyncio
import random
from telethon import events, version
from userbot import mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import channelparticipantsadmins
from userbot.cmdhelp import cmdhelp
from userbot.config import config
from . import *
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
defaultuser = str(alive_name) if alive_name else " #ɬųʄąąŋ_ơŋ_ʄıཞɛ 🔥⚡"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

tufaan = bot.uid

TUFAAN_IMG = Config.ALIVE_PIC or "https://te.legra.ph/file/efe721d64ca121757cc62.mp4"
pm_caption = "  __**𝚈𝚎𝚜 𝙼𝚊𝚜𝚝𝚎𝚛, 𝚈𝚘𝚞𝚛 𝚃𝚞𝚏𝚊𝚊𝚗𝙱𝚘𝚝 𝚒𝚜 𝚁𝚞𝚗𝚗𝚒𝚗𝚐 𝚂𝚖𝚘𝚘𝚝𝚑𝚕𝚢 !
**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f" ★➾ `My Master:` `{DEFAULTUSER}](tg://user?id={tufaan})}` \n"
pm_caption += f" ★➾ `Tufaan Version :` `{tufaanversion}`\n"
pm_caption += f" ★➾ `Sudo:` `{sudou}`\n"
pm_caption += f" ★➾ `Copyright:` TufaanBot(https://t.me/TheTufaanBot)\n"
pm_caption += f" ★➾ ` Branch:` [Master](https://GitHub.com/AKHIL-SI/TheTufaanBot)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔗 TUFAANBOT SOURCE 🔥](https://github.com/AKHIL-SI/TheTufaanBot) "

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, TUFAAN_IMG,caption=pm_caption)

CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()
