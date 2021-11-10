# Thanks to @D3_krish
# Porting in REBELUSERBOT by REBEL75

import asyncio
import random
from telethon import events, version
from userbot import ALIVE_NAME, REBELversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@Lynx_UserBot"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

REBEL = bot.uid

edit_time = 4
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/dcdd5186d27a015614b4e.jpg"
file2 = "https://telegra.ph/file/4abe4306eb84f561d67d0.jpg"
file3 = "https://telegra.ph/file/b221f9b6a883800185ce5.jpg"
file4 = "https://telegra.ph/file/b975803b122d543be3c0e.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥𝐋𝐲𝐧𝐱𝐁𝐨𝐭  𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                🔰ᗰᗩՏTᗴᖇ🔰\n      **『😈[{DEFAULTUSER}](tg://user?id={REBEL})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `𝚅𝚎𝚛𝚜𝚒𝚘𝚗:` `{REBELversion}`\n"
pm_caption += f"┣•➳➠ `𝚂𝚞𝚍𝚘:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `𝙲𝚑𝚊𝚗𝚗𝚎𝚕:` [𝙹𝙾𝙸𝙽](https://t.me/Lynx_UserBot)\n"
pm_caption += f"┣•➳➠ `𝙲𝚛𝚎𝚊𝚝𝚘𝚛:` [𝙻𝚢𝚗𝚡](https://t.me/Mr_developer_xd)\n"
pm_caption += f"┣•➳➠ `𝙼𝚛 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛:` [𝙽𝙸𝚂𝙷𝚄](https://t.me/Mr_developer_xd)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥𝐑𝐄𝐏𝐎🔥](https://github.com/Itz-UNKOWN-xd/Lynx-Bot) 🔹 [📜𝐋𝐢𝐜𝐞𝐧𝐬𝐞📜](https://github.com/Itz-UNKOWN-xd/Lynx-UserBot/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "rebel", None, "To check am i alive with your favorite alive pic"
).add()
