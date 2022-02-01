# ported by Skyla
# https://github.com/SkylaIND/Skyla-Userbot
# Hidup itu Asikin ajee gausa banyak tingkah


from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.to(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝚃𝙴𝙴𝙼𝙾 𝙳𝙸 𝙱𝙸𝚈𝙾𝙾")


@register(outgoing=True, pattern='^.btpm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝗞𝗔𝗞 𝗕𝗧𝗣𝗠 𝗖𝗛/𝗚𝗖 𝗕𝗨𝗔𝗧 𝗧𝗔𝗡𝗚𝗚𝗔𝗟 𝗕𝗘𝗥𝗔𝗣𝗔 𝗣𝗖 𝗔𝗝𝗔𝗔!!")


@register(outgoing=True, pattern='^.sl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("KAK BAGI SALDAN YANG LEBIH😁")


@register(outgoing=True, pattern='^.sy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("SAYA LUCU DAN SAYA DIAM..")


@register(outgoing=True, pattern='^.sm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("SASIMO AJA BELAGU ANJ..")


@register(outgoing=True, pattern='^.ga(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("GAMOOD HEHEHE..")


CMD_HELP.update({
    "santuy":
    ".to\
\nUsage: Gikes Tmo.\
\n\n.btpm\
\nUsage: Cari Btpm.\
\n\n.sl\
\nUsage: Cari Saldan.\
\n\n.sy\
\nUsage: Saya Lucu."
})


CMD_HELP.update({
    "santuy2":
    ".sm\
\nUsage: Lu Sasimo.\
\n\n.ga\
\nUsage: Aku Gamood."
})
