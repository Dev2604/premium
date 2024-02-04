from ub import app, clients
from pyrogram import filters, Client
import os
import re
import asyncio
import time
import config 
from pyrogram.types import Message
from ub.utils.database import add_user

API_ID = "6435225"
API_HASH = "4e984ea35f854762dcde906dce426c2d"

@app.on_message(filters.user(config.SUDOERS) & filters.command("clone"))
async def clone(app, msg: Message):
  if len(msg.command) < 2:
    return await msg.reply("Give A pyrogram session")
  else:
    session=msg.text.split(" ", 1)[1]
  try:
    await msg.delete()
    await msg.reply_text("Booting Your Client")
    cloner = Client(name="Clone", api_id=API_ID, api_hash=API_HASH, session_string=session, in_memory=True)
    await cloner.start()
    add_user(session)
    await msg.reply(f"Your Client Has Been Successfully As {cloner.me.first_name} ✅.")
  except Exception as e:
    await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
