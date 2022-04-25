import glob
from userbot import bot
from sys import argv
from userbot import TelegramClient
from userbot.exampleconfig import Var
from userbot.utils import load_module, start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from userbot import CMD_HNDLR

TELE = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        await bot.send_message(TELE, f"**Your TufaanBot has been deployed successfully\nType** `{CMD_HNDLR}alive` **to see if the bot is working.\n\nAdd** @{BOTNAME} **to your Tufaan Logger Group and make admin to work bot properly.**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished, no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("Your TufaanBot has been deployed successfully 😈 ")

print("Setting up your TufaanBot")
path = "userbot/plugins/mybot/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_mybot(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "userbot/plugins/mybot/pmbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("TGBot set up completely!")

print("TGBot set up - Level - Basic")
print("Tufaan has been fully deployed! Do Visit @TufaanBot_Support for any query")
bot.loop.run_until_complete(startup_log_all_done())

# Join Tufaan's Channel after deploying 🤐😅
# Come let us meet 😉

 try:
        await bot(JoinChannelRequest("@TufaanBot_Updates"))
    except BaseException:
        pass
 try:
        await bot(JoinChannelRequest("@TufaanBot_Support"))
    except BaseException:
         pass

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
