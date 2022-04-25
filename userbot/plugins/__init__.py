from telethon.tl.types import Channel

from userbot import *
from userbot import ALIVE_NAME, bot, telever
from userbot.exampleconfig import Config, Var

# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

ТυƒααηUser= str(ALIVE_NAME) if ALIVE_NAME else "@TufaanBot_Support"

tufaan = f"Tufaan Version: {telever}\n"
tufaan += f"Log Group: {log}\n"
tufaan += f"Assistant Bot: {bots}\n"
tufaan += f"Sudo: {sudo}\n"
tufaan += f"PMSecurity: {pm}\n"
tufaan += f"\nVisit @TufaanBot_Support for assistance.\n"
tufaanstats = f"{tufaan}"

TUFAAN_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# count total number of groups


async def tele_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
