from os import getenv

from dotenv import load_dotenv

load_dotenv()

# أضف هذه الإعدادات
COOKIE_PATH = "cookies.txt"
YOUTUBE_DL_OPTIONS = {
    'format': 'bestaudio/best',
    'cookiefile': COOKIE_PATH,
    'extractaudio': True,
    'audioformat': 'mp3',
    'noplaylist': True,
}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "3500"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/xl444")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/xl444")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))


FAILED = "https://graph.org/file/8882cbd7cc786826d9ecb.jpg"
