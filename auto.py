#Devs: @IkariS0_0 @KoraXD

from .. import app
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

CHEAT_BOT_ID = 123456789
CHEAT_BOT = @username
WAIFU_BOT_ID = 123456789
GROUP_ID = -123456789

#Devs: @IkariS0_0 @KoraXD

def character_name(message):
    if "Copy string:" in message.text:
        return message.text.split("Copy string: ")[1].split("\n")[0]
    else:
        return None

#Devs: @IkariS0_0 @KoraXD

@app.on_message(filters.user(BOT_ID) & filters.photo)
async def guess_photo(_, message):
    if "/secure" in message.caption:
        try:
            await app.forward_messages(CHEAT_BOT, message.chat.id, message.id)
        except Exception as e:
            await message.reply_text(f"ERROR - {e}")

#Devs: @IkariS0_0 @KoraXD

@app.on_message(filters.private & filters.user(CHEAT_BOT_ID) & filters.text & filters.incoming)
async def guess_text(_, message):
    try:
        char_name = character_name(message)
        if char_name:
            await app.send_message(chat_id=GROUP_ID, text=f"{char_name}")
    except Exception as e:
        await message.reply_text(f"ERROR - {e}")
