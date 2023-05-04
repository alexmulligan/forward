# config.py
# this file must be named config.py for the program to work properly

# === General Config ===

# Time to wait between checking for new notifications
SLEEP_TIME = 30

# If the notification title contains one of the below keywords, it will be handled. (i.e. 'outlook', 'chrome')
# An emtpy list disables this and handles all notifications
APP_WHITELIST = ['outlook', 'teams', 'chrome']

# Each notification will get forwarded to all the following outputs.  Currently supports 'console', 'telegram', 'email'
OUTPUTS = ['console']

# Enable/disable debug messages
DEBUG = False

# === Telegram config ===

ENABLE_TELEGRAM = False

# Token and Chat ID are from Telegram; TOKEN is from creating the telegram bot, CHAT_ID is the recipient to send message too
# See README.md for more information
TOKEN = 'YOUR_BOT_TOKEN_HERE'
CHAT_ID = 'YOUR_CHAT_ID_HERE'


# === Email config ===

ENABLE_EMAIL = True

# Email and password for account to send emails from.
# Not all email providers support email & password log in like this. See README.md for more info
EMAIL = 'notification_sender@email.com'
PASSWORD = 'password'

RECIPIENT = 'recipient_email@gemail.com'
