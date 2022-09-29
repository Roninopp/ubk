# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=76359, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="78ba6352dd5cdc166fdef5aa84ba7c67")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default="1BVtsOJUBu3_kEu_mV76-5FIKSgdBPlFXvTma7Fxyv96szkmXAkG6WT5Yi_P3sXZ11aVSvqFAAQZ5jCa9B-Mlb5uE3dustOUNgzjHRNFcTBxkMGfNZ7iD0kWIX8sTMrOOhD5wnUllCs3bpVxLWxxSiZfvVg66gq_ytKgk7MMw428Q9LN0DksGJPX3I3GZlvsFd1CKOFP-appcToR_nAAahsOtbB7aIu4IhbY8RYTo79k_m041xnGohdVgV9MkozgqGldx6osIIcUAji5t33AWB3o-ac6xDP5eLrTDRk3vCbkWo3F2W2QuO3z7Ex5cSqibgFYt7h1E_oDjgHFRoMqoL2TzsAvNsL8=")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default="redis-10625.c99.us-east-1-4.ec2.cloud.redislabs.com:10625"))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default="dplEdSkGkGs0WCs7J2XdGRSLgQL0HHGT")
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default="5420641611:AAFRadnL6Z16KVBIW72IyPl3V9OJ98YlmwI")
    LOG_CHANNEL = config("LOG_CHANNEL", default=-1001754175512, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default="ok")
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default="1BVtsOJUBu3_kEu_mV76-5FIKSgdBPlFXvTma7Fxyv96szkmXAkG6WT5Yi_P3sXZ11aVSvqFAAQZ5jCa9B-Mlb5uE3dustOUNgzjHRNFcTBxkMGfNZ7iD0kWIX8sTMrOOhD5wnUllCs3bpVxLWxxSiZfvVg66gq_ytKgk7MMw428Q9LN0DksGJPX3I3GZlvsFd1CKOFP-appcToR_nAAahsOtbB7aIu4IhbY8RYTo79k_m041xnGohdVgV9MkozgqGldx6osIIcUAji5t33AWB3o-ac6xDP5eLrTDRk3vCbkWo3F2W2QuO3z7Ex5cSqibgFYt7h1E_oDjgHFRoMqoL2TzsAvNsL8=")
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default="dplEdSkGkGs0WCs7J2XdGRSLgQL0HHGT")
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default="None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default="mongodb+srv://DARKAMAN:DARKAMAN@cluster0.snqhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
