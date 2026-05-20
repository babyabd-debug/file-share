#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler

#IMDb 
IMDB_API_KEY = 'k_6p68dybu'

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8686648515:AAFMke3sp70d-1IinyurlkTwl8oeWgzOJlM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "32381936"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "84b62a739a2f582d3594416eb7e6607f")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003947600023"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "8487637963 8374260942"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://nayixo5975:nayixo5975@cluster0.i93leyr.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1003982351683"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nthere, Welcome here ✨\n\nWe are happy to see you here.\n\nWe are a Brand who provide all kind of content to members with no cost.\n\nDon't forget to join channels/groups given below and get what you dream in your life. ✌🏻")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "8487637963 8374260942").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
