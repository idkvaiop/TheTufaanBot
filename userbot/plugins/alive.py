import asyncio
import random
from telethon import events, version
from userbot import mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import channelparticipantsadmins
from userbot.cmdhelp import cmdhelp
from userbot.config import config
from . import *
# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
defaultuser = str(alive_name) if alive_name else " #Ι¬Ε³ΚΔΔΕ_Ζ‘Ε_ΚΔ±ΰ½Ι π₯β‘"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

tufaan = bot.uid

TUFAAN_IMG = Config.ALIVE_PIC or "https://te.legra.ph/file/efe721d64ca121757cc62.mp4"
pm_caption = "  __**πππ πΌπππππ, ππππ πππππππ±ππ ππ πππππππ ππππππππ’ !
**__\n\n"

pm_caption += f"**ββββββββββββββββββββ**\n\n"
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += f" ββΎ `My Master:` `{DEFAULTUSER}](tg://user?id={tufaan})}` \n"
pm_caption += f" ββΎ `Tufaan Version :` `{tufaanversion}`\n"
pm_caption += f" ββΎ `Sudo:` `{sudou}`\n"
pm_caption += f" ββΎ `Copyright:` TufaanBot(https://t.me/TheTufaanBot)\n"
pm_caption += f" ββΎ ` Branch:` [Master](https://GitHub.com/AKHIL-SI/TheTufaanBot)\n"
pm_caption += f"ββββββββββββββββββββ\n"
pm_caption += " [π TUFAANBOT SOURCE π₯](https://github.com/AKHIL-SI/TheTufaanBot) "

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
