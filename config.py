import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Database to save your chats and stats... Get MongoDB:- 
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))

# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Zᴇᴅᴢᴇ ✘")

# Your User ID.
OWNER_ID = list(map(int, getenv("OWNER_ID", "5301800943").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5301800943").split()))

# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

# For customized or modified Repository
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/team-katil/lundkebaal")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL","https://t.me/katil_bots")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/katilsupport")

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "5000"))

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1000"))

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

# Set it True if you want to delete downloads after the music playout ends from your downloads folder
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "300"))

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "60"))

# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes

# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot.
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


# Images
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/ff3d94744211c796cf5bb.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/07b109ac650e5f4fec9e5.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/1dca3157eb1d637846d87.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/7dc2e0a1277c1dd43b40e.jpg"

STATS_IMG_URL = "https://telegra.ph/file/99b282829d8e877a099a6.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/29c8494278f990e910893.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/3df34a720f2d6d08f57c9.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/f6fcad691d6948d7a89af.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/61ecec3d3f8d1123998db.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/ae2ce86d990c42710c52c.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/7bc63654994a5d41bddf5.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/d68695ad86852583f1ce4.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/ade24dc9e43fbe5f73a04.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/07b109ac650e5f4fec9e5.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/ff3d94744211c796cf5bb.jpg"
