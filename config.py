import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    CHAT = os.environ.get('CHAT', None)
    USERS = os.environ.get('USERS', None)
    LINK_CHAT = os.environ.get('LINK_CHAT', None)
    ZIP_CHAT = os.environ.get('ZIP_CHAT', None)
    FILES_CHAT = os.environ.get('FILES_CHAT', None)
    NAMES_CHAT = os.environ.get('NAMES_CHAT', None)
    NAMES_TEXT_CHAT = os.environ.get('NAMES_TEXT_CHAT', None)
    

  
else:
  
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    CHAT = 0
    USERS = ""
    LINK_CHAT = 0
    ZIP_CHAT = 0
    FILES_CHAT = 0
    NAMES_CHAT = 0
    NAMES_TEXT_CHAT = 0

