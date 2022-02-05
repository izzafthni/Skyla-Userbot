# Sky Not
# by @Zxyune
# FROM Skyla-Userbot <https://github.com/SkylaIND/Skyla-Userbot>


from platform import uname
from userbot import ALIVE_NAME

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.syg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╭━━━╮\n"
                     "┃╭━╮┃\n"
                     "┃╰━━┳━━┳╮╱╭┳━━┳━╮╭━━╮\n"
                     "╰━━╮┃╭╮┃┃╱┃┃╭╮┃╭╮┫╭╮┃\n"
                     "┃╰━╯┃╭╮┃╰━╯┃╭╮┃┃┃┃╰╯┃\n"
                     "╰━━━┻╯╰┻━╮╭┻╯╰┻╯╰┻━╮┃\n"
                     "╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╭━╯┃\n"
                     "╱╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╰━━╯\n")


@register(outgoing=True, pattern='^.sas(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╔═══╗\n"
                     "║╔═╗║\n"
                     "║╚══╦══╦══╦╦╗╔╦══╗\n"
                     "╚══╗║╔╗║══╬╣╚╝║╔╗║\n"
                     "║╚═╝║╔╗╠══║║║║║╚╝║\n"
                     "╚═══╩╝╚╩══╩╩╩╩╩══╝\n")


CMD_HELP.update({
    "kata":
    ".syg\
\nUsage: .Tulisan Sayang\
\n\n.sas\
\nUsage: .Tulisan Sasimo"
})
