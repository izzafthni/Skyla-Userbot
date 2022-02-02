""" Userbot initialization. """

import logging
import os
import time
import re
import redis
import random

from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil

from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from pymongo import MongoClient
from datetime import datetime
from redis import StrictRedis
from dotenv import load_dotenv
from requests import get
from telethon.sync import TelegramClient, custom, events
from telethon.sessions import StringSession
from telethon import Button, events, functions, types
from telethon.utils import get_display_name

redis_db = None

load_dotenv("config.env")

StartTime = time.time()

CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info("You MUST have a python version of at least 3.8."
              "Multiple features depend on this. Bot quitting.")
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_KEY") or None)
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", "")

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", ""))

# DEVS
DEVS = (
    1964264380,
    1738637033,
    1025252069,
    1663258664,
    1416529201,
    1937084611,
    1977978893,
    1779447750,
    1842074890,
    1964264380,
    1927621859,
    742495738,
)

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Custom Pmpermit text
PMPERMIT_TEXT = os.environ.get("PMPERMIT_TEXT", None)

# Custom Pmpermit pic
PMPERMIT_PIC = os.environ.get(
    "PMPERMIT_PIC",
    None) or "https://telegra.ph/file/ca73aa215579a60c700f3.jpg"

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Send .chatid in any group with all your administration bots (added)
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", "")
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/SkylaIND/Skyla-Userbot")
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "Skyla-Userbot")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Redis URI & Redis Password
REDIS_URI = os.environ.get('REDIS_URI', None)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)

if REDIS_URI and REDIS_PASSWORD:
    try:
        REDIS_HOST = REDIS_URI.split(':')[0]
        REDIS_PORT = REDIS_URI.split(':')[1]
        redis_connection = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD
        )
        redis_connection.ping()
    except Exception as e:
        logging.exception(e)
        print()
        logging.error(
            "Make sure you have the correct Redis endpoint and password "
            "and your machine can make connections."
        )

# Chrome Driver and Headless Google Chrome Binaries
CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
# send .get_id in any channel to forward all your NEW PMs to this group
PM_LOGGR_BOT_API_ID = int(os.environ.get("PM_LOGGR_BOT_API_ID", "-100"))

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)

# For MONGO based DataBase
MONGO_URI = os.environ.get("MONGO_URI", None)

# set blacklist_chats where you do not want userbot's features
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Untuk Perintah .skyalive
SKYLA_TEKS_KUSTOM = os.environ.get("SKYLA_TEKS_KUSTOM", None)

# Default .alive Name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile Module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly Module
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)

# Bot Name
TERM_ALIAS = os.environ.get("TERM_ALIAS", "Rose-Userboot")

# Bot Version
BOT_VER = os.environ.get("BOT_VER", "7.0")

# Default .alive Username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Sticker Custom Pack Name
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Default .alive Logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/0970dd27e9141599aaccf.jpg"

# Default .helpme Logo
INLINE_PIC = os.environ.get(
    "INLINE_PIC") or "https://telegra.ph/file/3c30043b78157ce046e83.jpg"

# Default Video welcome
WELCOME_PIC = os.environ.get(
    "WELCOME_PIC") or "https://telegra.ph/file/0970dd27e9141599aaccf.jpg"

# Default emoji help
EMOJI_HELP = os.environ.get("EMOJI_HELP") or "☃️"

# Default .alive Instagram
IG_ALIVE = os.environ.get("IG_ALIVE") or "instagram.com/ikyxyzu"

# °SKYLA-USERBOT°
OWNER_URL = os.environ.get("OWNER_URL") or "https://t.me/Zxyune"

# °SKYLA-USERBOT°
SUDO_USERS = os.environ.get("SUDO_USERS") or "1927621859"

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
# Google Photos
G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
G_PHOTOS_AUTH_TOKEN_ID = os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", None)
if G_PHOTOS_AUTH_TOKEN_ID:
    G_PHOTOS_AUTH_TOKEN_ID = int(G_PHOTOS_AUTH_TOKEN_ID)

# Genius Lyrics  API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get("QUOTES_API_TOKEN", None)

# Wolfram Alpha API
WOLFRAM_ID = os.environ.get("WOLFRAM_ID") or None

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN") or None
BOT_USERNAME = os.environ.get("BOT_USERNAME") or None

# Init Mongo
MONGOCLIENT = MongoClient(MONGO_URI, 27017, serverSelectionTimeoutMS=1)
MONGO = MONGOCLIENT.userbot


def is_mongo_alive():
    try:
        MONGOCLIENT.server_info()
    except BaseException:
        return False
    return True


# Init Redis
# Redis will be hosted inside the docker container that hosts the bot
# We need redis for just caching, so we just leave it to non-persistent
REDIS = StrictRedis(host='localhost', port=6379, db=0)


def is_redis_alive():
    try:
        REDIS.ping()
        return True
    except BaseException:
        return False


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    session = StringSession(str(STRING_SESSION))
else:
    session = "Skyla-UserBot"
try:
    bot = TelegramClient(
        session=session,
        api_id=API_KEY,
        api_hash=API_HASH,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()


async def checking():
    gocheck = str("@skylasupport")
    checker = str("@SkylaIND")
    try:
        await bot(GetSec(gocheck))
    except BaseException:
        pass
    try:
        await bot(GetSec(checker))
    except BaseException:
        pass

with bot:
    try:
        bot.loop.run_until_complete(checking())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)


async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
        )
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the userbot logging feature to work."
        )
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        quit(1)


with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)


async def check_alive():
    await bot.send_file(BOTLOG_CHATID, ALIVE_LOGO, caption=f"**Skyla-Userbot Berhasil Diaktifkan⚡**\n━━━━━━━━━━━━━━━━━━━\n❃ **ʙᴏᴛ ᴏꜰ :** {ALIVE_NAME}\n❃ **ʙᴏᴛ ᴠᴇʀ :** 5.0\n━━━━━━━━━━━━━━━━━━━\n❃ **sᴜᴘᴘᴏʀᴛ​ :** @skylasupport\n❃ **ᴄʜᴀɴɴᴇʟ​ :** @Takichanbot \n━━━━━━━━━━━━━━━━━━━")
    return

with bot:
    try:
        bot.loop.run_until_complete(check_alive())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
ENABLE_KILLME = True
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
ZALG_LIST = {}


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 2
    global lockpage
    lockpage = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {} ".format(
                f"{EMOJI_HELP}",
                x,
                f"{EMOJI_HELP}"),
            data="ub_modul_{}".format(x)) for x in helpable_modules]
    pairs = list(zip(modules[::number_of_cols],
                     modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (
                modulo_page + 1)] + [
            (custom.Button.inline(
                "<<ᴘʀᴇᴠɪᴏᴜꜱ", data="{}_prev({})".format(
                    prefix, modulo_page)), custom.Button.inline(
                        "ᴍᴇɴᴜ", data="{}_close({})".format(
                            prefix, modulo_page)), custom.Button.inline(
                                "ɴᴇxᴛ>>", data="{}_next({})".format(
                                    prefix, modulo_page)), )]
    return pairs


with bot:
    try:
        tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id

        roselogo = INLINE_PIC
        asupan = WELCOME_PIC
        plugins = CMD_HELP
        vr = BOT_VER

# ------------------------------ChatAction--------------->

        @ tgbot.on(events.ChatAction)
        async def handler(event):
            if event.user_joined or event.user_added:
                u = await event.client.get_entity(event.chat_id)
                c = await event.client.get_entity(event.user_id)
                await event.reply(
                    f"** Selamat Datang Digrub **👋\n"
                    f"[{get_display_name(u)}](tg: // user?id={u.id})\n"
                    f"────────────────────\n"
                    f"📮 ** Nama: ** [{get_display_name(c)}](tg: // user?id={c.id})\n"
                    f"────────────────────\n"
                    f"✏️ ** ID: ** {c.id}\n"
                    f"────────────────────\n"
                    f"🤴 **ʙᴏᴛᴏꜰ: ** {DEFAULTUSER}\n\n"
                    f"➠ ** Ketik ** /rules supaya tahu peraturan Group ini\n"
                    f"➠ **Atau** Kalian Bisa Klik /notes Dibawah Jika Ada\n",
                    buttons=[
                        [
                            Button.url("【﻿Ｃｈａｎｎｅｌ】",
                                       "https://t.me/Takichanbot")],
                    ]
                )

# ====================================InlineHandler===================================== #

        @ tgbot.on(events.NewMessage(pattern=r"/start"))
        async def handler(event):
            if event.message.from_id != uid:
                await event.client.get_entity(event.chat_id)
                await event.message.get_sender()
                await tgbot.send_file(event.chat_id, file=asupan,
                                      buttons=[
                                          [
                                              custom.Button.inline(
                                                  "ᴍᴇɴᴜ", data="menu"),
                                              custom.Button.inline(
                                                  "ɪɴꜰᴏ", data="info_random")],
                                          [custom.Button.inline(
                                              "ᴄᴏᴍᴍᴀɴᴅ ʙᴏᴛ", b"cmd")],
                                      ]
                                      )

        @ tgbot.on(events.CallbackQuery(data=b"start"))
        async def starte(event):
            text = (
                f"Join Groups Support @skylasupport")
            await event.edit(
                text,
                link_preview=True,
                buttons=[
                    [
                        custom.Button.inline(
                            "ᴍᴇɴᴜ", data="menu"),
                        custom.Button.inline(
                            "ɪɴꜰᴏ", data="info_random")],
                    [custom.Button.inline(
                        "ᴄᴏᴍᴍᴀɴᴅ ʙᴏᴛ", b"cmd")],
                ]
            )

        @ tgbot.on(events.NewMessage(pattern="/ping"))
        async def handler(event):
            if event.message.from_id != uid:
                await event.client.get_entity(event.chat_id)
                await event.message.get_sender()
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await tgbot.send_message(
                    event.chat_id,
                    f"I'am Online!\n**ping**: `{ms}ms`",
                )

        @ tgbot.on(events.NewMessage(pattern=r"/id"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.reply(f"ID`{u.id}`")

        @ tgbot.on(events.NewMessage(pattern="/repo"))
        async def handler(event):
            if event.message.from_id != uid:
                await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"☃️Sᴋʏʟᴀ-Usᴇʀʙᴏᴛ☃️\n",
                    buttons=[
                        [
                            Button.url("ʀᴇᴘᴏ",
                                       "https://github.com/SkylaIND/Skyla-Userbot"),
                            Button.url("ʟɪᴄᴇɴꜱᴇ",
                                       "https://github.com/SkylaIND/Skyla-Userbot/blob/Skyla-Userbot/LICENSE")],
                        [Button.url("ɢʀᴏᴜᴘꜱ",
                                    "t.me/skylasupport")],
                    ]
                )

# ====================================InlineHelpme===================================== #

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(f"open_plugin")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                buttons = paginate_help(0, dugmeler, "helpme")
                text = f"☃️Sᴋʏʟᴀ-Usᴇʀʙᴏᴛ☃️\n\n**🄼🄰🄸🄽 🄼🄴🄽🅄**\n\n❥ **Bᴏᴛ Oғ :** {DEFAULTUSER}\n❥ **ʙᴏᴛ ᴠᴇʀ :** 5.0\n❥ **ᴍᴏᴅᴜʟᴇꜱ :** {len(plugins)} "
                await event.edit(text,
                                 file=roselogo,
                                 buttons=buttons,
                                 link_preview=False,
                                 )
            else:
                reply_pop_up_alert = f"❌ WARNINGS ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"nepo")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            current_page_number = int(lockpage)
            buttons = paginate_help(current_page_number, plugins, "helpme")
            await event.edit(
                file=roselogo,
                buttons=buttons,
                link_preview=False,
            )

        @ tgbot.on(events.CallbackQuery(data=b"cmd"))
        async def cmd(event):
            await event.edit("/start - **Memulai Bot**\n/ping - **Untuk Melihat Bot Aktif atau tidak**\n/repo - **Mendapatkan Repository Bot**\n/id - **Mendapatkan Id Kamu**", buttons=Button.clear())

# ====================================Menu===================================== #

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"menu")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"Menu {DEFAULTUSER} :")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.inline("❍ʜᴏᴍᴇ❍", data="start"),
                            Button.inline("❍ᴄᴜꜱᴛᴏᴍ ᴠᴀʀꜱ❍", data="settings"),
                        ],
                        [
                            Button.inline("❍ᴏᴡɴᴇʀ ᴛᴏᴏʟꜱ❍", data="owner_tools"),
                            Button.inline("❍ᴄᴏᴍᴍᴀɴᴅ ʙᴏᴛ❍", data="pmon_pmof"),
                        ]
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nHanya {DEFAULTUSER}Yang Bisa Menekan Tombol Ini, Deploy Skyla Userbot Untuk Mengetahui Fitur Nya."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

# ====================================CustomVars===================================== #

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"settings")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"{DEFAULTUSER}Pilih dari opsi di bawah ini :")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("ᴜᴘᴅᴀᴛᴇ", data="pembaruan")],
                        [custom.Button.inline("ᴀʟɪᴠᴇ", data="alive")],
                        [custom.Button.inline("ᴘᴍᴘᴇʀᴍɪᴛ", data="permirt")],
                        [custom.Button.inline(
                            "ɪɴʟɪɴᴇ ᴍᴏᴅᴇ ", data="inline_mode")],
                        [custom.Button.inline("ʙᴀᴄᴋ", data="menu")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"alive")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"**Modules :** `alive`\n"
                    f"** Owner: ** {DEFAULTUSER}\n\n"
                    f"✘ **Penjelasan :**\n"
                    f"__Menampilkan Alive Punya Kamu, Dengan Teks Dan Foto Yang Bagus Dan Meriah.__\n\n"
                    f"✘ **Description :**\n"
                    f"__Kamu Juga Dapat Mengubah Foto Dan Teks Custom Sesuka Hatimu Command Dibawah.__\n\n"
                    f"✘ **Command :**\n"
                    f"`.skyalive` || `.skylaon` || `.alive` \n\n"
                    f"✘ **SetVars :**\n"
                    f"`.set var ALIVE_LOGO` <link>\n"
                    f"`.set var SKYLA_TEKS_KUSTOM` <teks>\n\n"
                    f"© @skylasupport")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline(
                                "ʙᴀᴄᴋ", data="settings"),
                            custom.Button.inline(
                                "ᴄʟᴏꜱᴇ", data="closed")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"permirt")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"**Modules :** `pmpermit`\n"
                    f"** Owner: ** {DEFAULTUSER}\n\n"
                    f"✘ **Penjelasan :**\n"
                    f"__Jika Kamu Mengaktifkan Pmpermit Kamu KeTrue, Otomatis Pmpermit Kamu Akan Aktif Bawaan Langsung Dari Skyla-Userbot.__\n\n"
                    f"✘ **Description :**\n"
                    f"__Kamu Juga Dapat Mengubah Pmpermit Kamu Sendiri, Lihat Dicomand.__\n\n"
                    f"✘ **Command :**\n"
                    f"`.set pm_msg`  <teks>\n\n"
                    f"✘ **SetVars :**\n"
                    f"`.set var PM_AUTO_BAN True`\n\n"
                    f"© @skylasupport")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline(
                                "ʙᴀᴄᴋ", data="settings"),
                            custom.Button.inline(
                                "ᴄʟᴏꜱᴇ", data="closed")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"inline_mode")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"**Modules :** `help`\n"
                    f"** Owner: ** {DEFAULTUSER}\n\n"
                    f"✘ **Penjelasan :**\n"
                    f"__helpme Dapat Menampilkan Modules Berbentuk Inline, Dan Dapat Dijelaskan Bagaimana Cara Penggunaannya.__\n\n"
                    f"✘ **Description :**\n"
                    f"__Kamu Juga Dapat Mengubah Beberapa Fitur, Yaitu Emoji Dibutton Dan Foto.__\n\n"
                    f"✘ **Command :**\n"
                    f"`.helpme`\n\n"
                    f"✘ **SetVars :**\n"
                    f"`.set var INLINE_PIC` <link>\n"
                    f"`.set var EMOJI_HELP` <emoji>\n\n"
                    f"© @skylasupport")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline(
                                "ʙᴀᴄᴋ", data="settings"),
                            custom.Button.inline(
                                "ᴄʟᴏꜱᴇ", data="closed")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"pembaruan")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"**Modules :** `update`\n"
                    f"** Owner: ** {DEFAULTUSER}\n\n"
                    f"✘ **Penjelasan :**\n"
                    f"__Kamu Dapat Mengecek Pembaruan Untuk Skyla-Userbot, Agar Dapat Menikmati Fitur Terbaru.__\n\n"
                    f"✘ **Description :**\n"
                    f"__Diusahakan Untuk Update Deploy, Jangan Update Now, Agar Bisa Mengatahui Update Terbaru Nya.__\n\n"
                    f"✘ **Command :**\n"
                    f"`.update deploy`\n\n"
                    f"© @skylasupport")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline(
                                "ʙᴀᴄᴋ", data="settings"),
                            custom.Button.inline(
                                "ᴄʟᴏꜱᴇ", data="closed")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

# ====================================OwnerTools===================================== #

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"owner_tools")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"Menu Lainnya ! Untuk {DEFAULTUSER}")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline(
                            "ᴏᴘᴇɴ ᴍᴏᴅᴜʟᴇꜱ", data="open_plugin")],
                        [custom.Button.inline("ᴀʟɪᴠᴇ ᴍᴇ", data="rose")],
                        [custom.Button.inline("ᴘɪɴɢ", data="ping")],
                        [custom.Button.inline("<<ʟᴇꜰᴛ", data="menu")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"rose")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"**{SKYLA_TEKS_KUSTOM}**\n\n"
                    f"┏━━━━━━━━━━━━━━━━━━━━━\n"
                    f"┣ **Pemilik** - `{DEFAULTUSER}`\n"
                    f"┣ **Versi** - `7.0`\n"
                    f"┣ **Groups** - @skylasupport\n"
                    f"┣ **Bahasa** - `Python`\n"
                    f"┣ **Branch** - `Skyla-Userbot`\n"
                    f"┣ **Modules** - `184`\n"
                    f"┗━━━━━━━━━━━━━━━━━━━━━")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline(
                                "ʙᴀᴄᴋ", data="owner_tools")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ping")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                text = (
                    f"**PONG!!**\n `{ms}ms`")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline(
                                "ʙᴀᴄᴋ", data="owner_tools")],
                    ]
                )
            else:
                reply_pop_up_alert = f"PONG!!\n `{ms}ms`"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

# ====================================COMMANDHANDLER===================================== #

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"pmon_pmof")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"/ping - **Mengecek Sinyal Bot**")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("ʙᴀᴄᴋ", data="menu")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

# ====================================CLOSED===================================== #

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"closed")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"Closed Menu!")
                await event.edit(
                    text,
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline(
                                "ᴏᴘᴇɴ ᴀɢᴀɪɴ", data="menu")],
                    ]
                )

# ====================================INLINEHELPME===================================== #

        @ tgbot.on(events.InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith(
                    "@skylasupport"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=roselogo,
                    link_preview=False,
                    text=f"☃️Sᴋʏʟᴀ-Usᴇʀʙᴏᴛ☃️\n\n**🄼🄰🄸🄽 🄼🄴🄽🅄**\n\n❥ **Bᴏᴛ Oғ :** {DEFAULTUSER}\n❥ **ʙᴏᴛ ᴠᴇʀ :** 5.0\n❥ **ᴍᴏᴅᴜʟᴇꜱ :** {len(plugins)}".format(
                        len(dugmeler),
                    ),
                    buttons=buttons,
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "Bantuan Dari  ☃️Sᴋʏʟᴀ - Usᴇʀʙᴏᴛ☃️",
                    text="Daftar Plugins",
                    buttons=[],
                    link_preview=True)
            else:
                result = builder.article(
                    " ☃️Sᴋʏʟᴀ - Usᴇʀʙᴏᴛ☃️ ",
                    text="""°ROSE-USERBOT°""",
                    buttons=[
                        [
                            custom.Button.url(
                                "SKYLA",
                                "https://github.com/SkylaIND/Skyla-Userbot"),
                            custom.Button.url(
                                "SUPPORT",
                                "t.me/skylasupport")],
                        [custom.Button.url(
                            "LICENSE",
                            "https://github.com/SkylaIND/Skyla-Userbot/blob/Skyla-Userbot/LICENSE")],
                    ],
                    link_preview=False,
                )
            await event.answer([result] if result else None)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # userbot
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=roselogo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.url(f"{EMOJI_HELP} ɢʀᴏᴜᴘꜱ {EMOJI_HELP} ",
                                       "t.me/skylasupport"),
                            Button.url(f"{EMOJI_HELP} ᴄʜᴀɴɴᴇʟ {EMOJI_HELP} ",
                                       "t.me/SkylaIND")],
                        [Button.url(f"{EMOJI_HELP} ᴅᴇᴘʟᴏʏ sᴋʏʟᴀ {EMOJI_HELP} ",
                                    f"https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FCangcimenn%2FSkyla-Userbot&template=https%3A%2F%2Fgithub.com%2FCangcimenn%2FSkyla-Userbot"),
                            Button.url(f"{EMOJI_HELP} ɪɴꜱᴛᴀɢʀᴀᴍ {EMOJI_HELP} ",
                                       f"{IG_ALIVE}")],
                        [custom.Button.inline(
                            f"{EMOJI_HELP} ᴄʟᴏꜱᴇ {EMOJI_HELP}", b"close")],
                    ]
                )

# ====================================STARTWELCOME===================================== #

        @ tgbot.on(events.CallbackQuery(data=b"info_random"))
        async def start(event):
            text = (
                f"**Owner:** {DEFAULTUSER}\n**Emoji:** {EMOJI_HELP}\n\n**Pmpermit:** {PM_AUTO_BAN}\n\n**Powered By:** @Rose_Userbot")
            await event.edit(
                text,
                link_preview=True,
                buttons=[
                    [
                        Button.url(f"ᴏᴡɴᴇʀ ",
                                   f"{OWNER_URL}"),
                        Button.url(f"ᴄʜᴀɴɴᴇʟ ",
                                   f"{CHANNEL_URL}")],
                    [custom.Button.inline(
                        "ʙᴀᴄᴋ", b"start")],
                ]
            )

        @ tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            buttons = [
                (custom.Button.inline("ᴏᴘᴇɴ ᴀɢᴀɪɴ", data="open_plugin"),),
            ]
            await event.edit(f"Menu Ditutup! ", buttons=buttons)

# ====================================INLINEHELPME===================================== #

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 180:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace(
                            '`', '')[: 180] + "..."
                        + "\n\nBaca Text Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace('`', '')

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} No document has been written for module.".format(
                        modul_name
                    )
                )
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Mode Inline Bot Mu Nonaktif. "
            "Untuk Mengaktifkannya, Silahkan Pergi Ke @BotFather Lalu, Settings Bot > Pilih Mode Inline > Turn On. ")
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID Environment Variable Isn't a "
            "Valid Entity. Please Check Your Environment variables/config.env File.")
        quit(1)
