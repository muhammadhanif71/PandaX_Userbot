import os
from typing import Set
from .sql_helper import sqldb as SqL
from telethon.tl.types import ChatBannedRights
import heroku3
from dotenv import load_dotenv
from distutils.util import strtobool

if os.path.exists("local.env"):
    load_dotenv("local.env")

def fetch_heroku_git_url(api_key, app_name):
    if not api_key:
        return None
    if not app_name:
        return None
    heroku = heroku3.from_key(api_key)
    try:
        heroku_applications = heroku.apps()
    except:
        return None
    heroku_app = None
    for app in heroku_applications:
        if app.name == app_name:
            heroku_app = app
            break
    if not heroku_app:
        return None
    return heroku_app.git_url.replace("https://", "https://api:" + api_key + "@")





class Config(object):
    LOGGER = True
    STRING_SESSION3 = os.environ.get("SESSION3") or None
  
    STRING_SESSION2 = os.environ.get("SESSION2") or None
    ALIVE_NAME = SqL.getdb("ALIVE_NAME") or os.environ.get("ALIVE_NAME", None)
    APP_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    DB_URI = os.environ.get("DATABASE_URL", None)
    PYROGRAM_SESSION = os.environ.get("PYROGRAM_SESSION", None)
    MONGO_URI = os.environ.get("MONGO_URI", None)
    STRING_SESSION = os.environ.get(
        "SESSION", None
    )
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN") or os.environ.get(
        "TG_BOT_TOKEN_BF_HER", None
    )
    TG_BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    TZ = SqL.getdb("TZ") or os.environ.get("TZ", "Asia/Jakarta") 
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/ilhammansiz/PandaX_Userbot.git"
    ) 
    AUTONAME = os.environ.get("AUTONAME", None)
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID") or 0)
    PRIVATE_CHANNEL_BOT_API_ID = int(os.environ.get("PRIVATE_CHANNEL_BOT_API_ID") or 0)
    HEROKU_API_KEY = os.environ.get("HEROKU_API", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
    MAX_FLOOD_IN_PMS = int(os.environ.get("MAX_FLOOD_IN_PMS", 5))
    PM_LOGGER_GROUP_ID = int(
        os.environ.get("PM_LOGGER_GROUP_ID")
        or os.environ.get("PM_LOGGR_BOT_API_ID")
        or 0
    )

    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL") or 0)
    CUSTOM_ALIVE_TEXT = os.environ.get("CUSTOM_ALIVE_TEXT", None)
    CUSTOM_ALIVE_EMOJI = os.environ.get("CUSTOM_ALIVE_EMOJI", None)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "pandauserbot")
    THUMB_IMAGE = os.environ.get(
        "THUMB_IMAGE", "https://telegra.ph/file/0c571ae6dcb68ea2bdf49.jpg"
    )

    PANDA_HELP_LOGO = os.environ.get(
        "PANDA_HELP_LOGO", None
    )
    UB_BLACK_LIST_CHAT = {
        int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    }
    NO_LOAD = [x for x in os.environ.get("NO_LOAD", "").split()]
    # For custom alive pic
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
    # for Custom pmpermit pic
    PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
    # for custom pic for .digitalpfp
    DIGITAL_PIC = os.environ.get("DIGITAL_PIC", None)
    # your default pic telegraph link
    DEFAULT_PIC = os.environ.get("DEFAULT_PIC", None)
    # set this with your default bio
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    # set this with your deafult name
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)
    HELP_TEXT_INLINE = os.environ.get("HELP_TEXT_INLINE", None)
    # forcustomizing pmpermit text
    CUSTOM_PMPERMIT_TEXT = os.environ.get("CUSTOM_PMPERMIT_TEXT", None)
    # number of rows of buttons to be displayed in .help command
    NO_OF_ROWS_IN_HELP = int(os.environ.get("NO_OF_ROWS_IN_HELP", 5))
    # number of columns of buttons to be displayed in .helpme command
    NO_OF_COLUMNS_IN_HELP = int(os.environ.get("NO_OF_COLUMNS_IN_HELP", 2))
    # emoji to be displayed in .help
    EMOJI_TO_DISPLAY_IN_HELP = os.environ.get("EMOJI_TO_DISPLAY_IN_HELP", "✅")
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = SqL.getdb("COMMAND_HAND_LER") or os.environ.get("COMMAND_HAND_LER", r".")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r".")
    # set this with required folder path to act as download folder
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "downloads")
    # set this with required folder path to act as temparary folder
    TEMP_DIR = os.environ.get("TEMP_DIR", "./temp/")
    # For custom stickerpack names
    CUSTOM_STICKER_PACKNAME = os.environ.get("CUSTOM_STICKER_PACKNAME", None)
    # time to update autoprofile cmds
    CHANGE_TIME = int(os.environ.get("CHANGE_TIME", 60))
    # SpamWatch, CAS, SpamProtection ban Needed or not
    ANTISPAMBOT_BAN = os.environ.get("ANTISPAMBOT_BAN", False)
    # is dual logging needed or not true or false
    DUAL_LOG = os.environ.get("DUAL_LOG", False)
    # progress bar progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "▰")
    UNFINISHED_PROGRESS_STR = os.environ.get("UNFINISHED_PROGRESS_STR", "▱")
    DEVS = os.environ.get("DEVS", "*")
    SUDO_ENABLED = False
    # API VARS FOR USERBOT
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture for screen shot
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    # This is required for the speech to text plugin. Get your USERNAME from
    # https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    # Genius lyrics get this value from https://genius.com/developers both has
    GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
    # Get your own API key from https://www.remove.bg/
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
    G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
    G_DRIVE_INDEX_LINK = os.environ.get("G_DRIVE_INDEX_LINK", None)
    TG_2STEP_VERIFICATION_CODE = os.environ.get("TG_2STEP_VERIFICATION_CODE", None)
    WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "IN")
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    
    RANDOM_STUFF_API_KEY = os.environ.get("RANDOM_STUFF_API_KEY", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    DEEP_AI = os.environ.get("DEEP_AI", None)
    ALLOW_NSFW = os.environ.get("ALLOW_NSFW", "False")
    MAX_MESSAGE_SIZE_LIMIT = 4095
    
    LOAD = []
    
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get(
        "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
    )
    
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
        "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )
    
    COUNTRY = str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    
    UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "PandaUserbot")
    
    SUDO_USERS: Set[int] = set()
    PANDAUBLOGO = None
    LOG_GRP = PRIVATE_GROUP_BOT_API_ID
    COMMAND_HANDLER = COMMAND_HAND_LER
    SUDO_USERS = SUDO_USERS
    AFS = list(SUDO_USERS)
    CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "🐼")
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    FBAN_GROUP = int(os.environ.get("FBAN_GROUP", False))
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/ilhammansiz/PandaX_Userbot"
    )
    ALIVE_IMG = os.environ.get(
        "ALIVE_IMG", "https://telegra.ph/file/336d811bce4f1d1053fbf.jpg"
    )
    U_BRANCH = "PandaUserbot"
    HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
    V_T_KEY = os.environ.get("VIRUSTOTAL_API_KEY", None)
    TAG_LOGGER = os.environ.get("TAG_LOGGER", False)
    PM_PSW = bool(strtobool(str(os.environ.get("PM_PSW", True))))
    MAIN_NO_LOAD = [x for x in os.environ.get("MAIN_NO_LOAD", "").split(',')]
    XTRA_NO_LOAD = [x for x in os.environ.get("XTRA_NO_LOAD", "").split(',')]
    DISABLED_SUDO_CMD_S = os.environ.get("DISABLED_SUDO_CMD_S", None)
    ENABLE_WAIFU_FOR_ALL_CHATS = bool(strtobool(str(os.environ.get("ENABLE_WAIFU_FOR_ALL_CHATS", False))))
    CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH", "/usr/bin/chromedriver")
    CHROME_BIN_PATH = os.environ.get("CHROME_BIN_PATH", "/usr/bin/google-chrome-stable")
    TZ = os.environ.get("TZ", "Asia/Jakarta")
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    LOAD_UNOFFICIAL_PLUGINS = bool(strtobool(str(os.environ.get("LOAD_UNOFFICIAL_PLUGINS", False))))



class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
