import time

from userbot import ALIVE_NAME, StartTime, REBELversion
from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "Lynx User"
REBEL_IMG = "https://te.legra.ph/file/ea7e4fa36eab1a2d62fd8.jpg"
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "𝐋𝐞𝐠𝐞𝐧𝐝𝐚𝐫𝐲_𝐀𝐅_𝐋𝐲𝐧𝐱𝐁𝐨𝐭"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="ly$"))
@bot.on(sudo_cmd(pattern="ly$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if REBEL_IMG:
        REBEL_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        REBEL_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"
        REBEL_caption += f"__**𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂**__\n\n"
        REBEL_caption += f"**❥︎ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙼 :** `1.15.0`\n"
        REBEL_caption += f"**❥︎ 𝙻𝚢𝚗𝚡𝙱𝚘𝚝 :**`{REBELversion}`\n"
        REBEL_caption += f"**❥︎ 𝚄𝙿𝚃𝙸𝙼𝙴   :** `{uptime}\n`"
        REBEL_caption += f"**❥︎ 𝙾𝚆𝙽𝙴𝚁    :** {mention}\n"
        REBEL_caption += f"**❥︎ 𝙳𝚎𝚟      :** [Mr.Developer](https://t.me/Mr_developer_xd)\n"
        await alive.client.send_file(
            alive.chat_id, REBEL_IMG, caption=REBEL_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ \n"
            f"__**𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂**__\n\n"
            f"**❥︎ 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 :** `1.15.0`\n"
            f"**❥︎ 𝙻𝚢𝚗𝚡𝙱𝚘𝚝 :** `{REBELversion}`\n"
            f"**❥︎ 𝚄𝙿𝚃𝙸𝙼𝙴      :** `{uptime}\n`"
            f"**❥︎ 𝙾𝚆𝙽𝙴𝚁        :** {mention}\n",
            f"**❥︎ 𝙳𝚎𝚟      :** [Mr.Developer](https://t.me/Mr_developer_xd)\n"
        )
