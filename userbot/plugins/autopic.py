

import asyncio

import os
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from userbot import *
from userbot import AUTO_PIC_FONT, AUTOPIC_FONT_COLOUR, AUTOPIC_TEXT, CMD_HELP

fntz = str(AUTO_PIC_FONT) if AUTO_PIC_FONT else "DejaVuSans.ttf"
FONT_FILE_TO_USE = f"resources/fonts/{fntz}"
AUTOPIC_TEXT = (
    str(AUTOPIC_TEXT)
    if AUTOPIC_TEXT
    else "Life Is too Short.\n And so is your TG account."
)
COLOUR = str(AUTOPIC_FONT_COLOUR) if AUTOPIC_FONT_COLOUR else (255, 255, 255)


@userbot.on(admin_cmd(pattern="autopic"))
async def autopic(event):
    await event.edit("**Autopic has been enabled!!!**")
    a = await event.get_reply_message()
    downloaded_file_name = "userbot/original_pic.png"
    await telebot.download_media(a, downloaded_file_name)
    photo = "telebot/photo_pfp.png"
    while True:
        shutil.copy(downloaded_file_name, photo)
        current_time = datetime.now().strftime(
            f"Time: %H:%M \nDate: %d.%m.%y \n{AUTOPIC_TEXT}"
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        color = COLOUR
        drawn_text.text((95, 250), current_time, font=fnt, fill=color)
        img.save(photo)
        file = await event.client.upload_file(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(photo)
            await asyncio.sleep(60)
        except BaseException:
            return


CMD_HELP.update(
    {"autopic": ".autopic <reply to pic>\nUse - Auto changing dp, with time and date."}
)
