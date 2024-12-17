import json
import os


def get_user_list(config, key):
    with open("{}/KING/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    API_HASH = "45aabfac" # API_HASH from my.telegram.org
    API_ID = 62 # API_ID from my.telegram.org

    BOT_ID = 521 # BOT_ID
    BOT_USERNAME = "KING" # BOT_USERNAME

    MONGO_DB_URL = "mongodb://username:password@localhost:27017/emi?directConnection=true&authSource=admin" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "SpiralTechDivision" # Support Chat Username
    UPDATE_CHANNEL = "SpiralUpdates" # Update Channel Username
    START_PIC = "https://pic-bstarstatic.akamaized.net/ugc/9e98b6c8872450f3e8b19e0d0aca02deff02981f.jpg@1200w_630h_1e_1c_1f.webp" # Start Image
    DEV_USERS = [6040984893, 6461051572, 7107018652] # Dev Users
    TOKEN = "57375" # Bot Token from @BotFather

    EVENT_LOGS = -10093 # Event Logs Chat ID
    OWNER_ID = 6040984893 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "Emilia" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    ORIGINAL_EVENT_LOOP = True # Do not Change


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
