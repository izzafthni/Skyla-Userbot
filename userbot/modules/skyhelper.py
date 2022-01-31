""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Semua Perintah Bot Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/Zxyune)"
        "\n[Repo](https://github.com/SkylaIND/Skyla-Userbot)"
        "\n[Instagram](instagram.com/ikyxyzu)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Kayzyu/Kayzu-Ubot/Kayzu-Ubot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.lhelp`\
\nUsage: Bantuan Untuk Skyla-Userbot.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
})
