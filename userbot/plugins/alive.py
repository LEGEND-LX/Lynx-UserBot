# Thanks to @D3_krish
# Porting in REBELUSERBOT by REBEL75

import asyncio
import random
from telethon import events, version
from userbot import ALIVE_NAME, REBELversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€π€
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
pm_caption = "  __**π₯π₯ππ²π§π±ππ¨π­  ππ ππππππ₯π₯**__\n\n"

pm_caption += f"**βββββββββββββββββββββββββββ**\n\n"
pm_caption += (
    f"                π°α°α©ΥTα΄απ°\n      **γπ[{DEFAULTUSER}](tg://user?id={REBEL})πγ**\n\n"
)
pm_caption += f"βββββββββββββββββββ\n"
pm_caption += f"β£β’β³β  `ππππππππ:` `{version.__version__}` \n"
pm_caption += f"β£β’β³β  `πππππππ:` `{REBELversion}`\n"
pm_caption += f"β£β’β³β  `ππππ:` `{sudou}`\n"
pm_caption += f"β£β’β³β  `π²ππππππ:` [πΉπΎπΈπ½](https://t.me/Lynx_UserBot)\n"
pm_caption += f"β£β’β³β  `π²ππππππ:` [π»π’ππ‘](https://t.me/Mr_developer_xd)\n"
pm_caption += f"β£β’β³β  `πΌπ π³ππππππππ:` [π³ππ](https://t.me/Mr_developer_xd)\n"
pm_caption += f"βββββββββββββββββββ\n"
pm_caption += " [π₯πππππ₯](https://github.com/Itz-UNKOWN-xd/Lynx-Bot) πΉ [πππ’πππ§π¬ππ](https://github.com/Itz-UNKOWN-xd/Lynx-UserBot/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.lynx$")
@bot.on(admin_cmd(outgoing=True, pattern="lynx$"))
@bot.on(sudo_cmd(pattern="lynx$", allow_sudo=True))
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
    

    """ For .lynx command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("lynx").add_command(
  "lynx", None, "To check am i alive"
).add_command(
  "ly", None, "To check am i alive with your favorite alive pic"
).add()
