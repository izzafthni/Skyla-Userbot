# Sky Not
# by @Zxyune
# FROM Skyla-Userbot <https://github.com/SkylaIND/Skyla-Userbot>


from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================
