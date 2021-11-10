from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, REBELversion
from pathlib import Path
import asyncio
import telethon.utils

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



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
        print("Initialisation finished with no errors")
        print("🔰𝐒𝐭𝐚𝐫𝐭 𝐋𝐲𝐧𝐱𝐁𝐨𝐭🔰")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("⚡𝐋𝐲𝐧𝐱𝐁𝐨𝐭 𝐬𝐭𝐚𝐫𝐭𝐮𝐩 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞⚡")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""𝐇𝐞𝐥𝐥𝐨 𝐬𝐢𝐫 𝐢 𝐚𝐦 𝐋𝐘𝐍𝐗𝐁𝐎𝐓!! 𝐋𝐘𝐍𝐗𝐁𝐎𝐓𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :- {REBELversion} 𝐘𝐎𝐔𝐑 𝐋𝐘𝐍𝐗𝐁𝐎𝐓 𝐈𝐒 𝐑𝐄𝐀𝐃𝐘! 𝐅𝐎𝐑 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐁𝐎𝐓 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐎𝐑 𝐍𝐎𝐓 𝐏𝐋𝐄𝐀𝐒𝐄 𝐓𝐘𝐏𝐄 (.𝐚𝐥𝐢𝐯𝐞/.𝐩𝐢𝐧𝐠) 𝐄𝐍𝐉𝐎𝐘 𝐘𝐎𝐔𝐑 𝐁𝐎𝐓! 𝐉𝐎𝐈𝐍 𝐅𝐎𝐑 𝐌𝐎𝐑𝐄 𝐅𝐔𝐓𝐔𝐑𝐄 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 @𝐋𝐘𝐍𝐗𝐁𝐎𝐓_𝐂𝐇𝐀𝐓 .""")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
