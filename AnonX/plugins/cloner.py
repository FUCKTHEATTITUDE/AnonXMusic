import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
import random
from random import choice
from config import API_ID, API_HASH , MUSIC_BOT_NAME
from AnonX import client as sys
from AnonX import app
import config
from strings import get_command
from ..logging import LOGGER
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid



@app.on_message(filters.private & filters.command("clone"))
async def clone(bot, msg: Message):
    chat = msg.chat.id
    text = await msg.reply("Usage:\n\n /clone token")
    cmd = msg.get_command
    phone = msg.get_command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone,plugins={"root": "AnonX.plugins"})
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \n\n Now Add Your Bot And Assistant @PREMIUMMUSICPLAYER1 To Your Chat!\n\nThanks for Cloning.")
        APP_USERNAME = user.username
        await sys.send_message(APP_USERNAME, "/start")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
#End
##This code fit with every pyrogram Codes just import then @Client Xyz!


