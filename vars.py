from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "N2 Auto Reply Bot")
API_ID = 26368462
API_HASH = "37727a29bfafc1a5f01224ca29bc2435"
USER_SESSION = environ.get("USER_SESSION", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074744533"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1001232792540 -1001288657204 -1002629654353').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7582905564').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
