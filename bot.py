import sys
import time
from datetime import timedelta
import pprint
import telepot
import config

def handle(msg):
    # Find out who is messaging the bot
    uid = msg["from"]["id"]

    # First we make sure you are an authorized user
    if uid == config.masteruser:
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(msg["text"])
        # Lets make sure the chat is private and we are dealing with text only
        if content_type == 'text' and chat_type == 'private':
            # Check system uptime
            if msg["text"] == "/uptime":
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.readline().split()[0])
                    uptime_string = str(timedelta(seconds = uptime_seconds))
                # Send uptime String
                bot.sendMessage(uid, uptime_string)
            else:
                pass
            if msg["text"] == "/help":
                msg = ("Current commands suppported by this bot: \n"
                       "/uptime: Return current system uptime")
                bot.sendMessage(uid, msg)
            else:
                pass
        else:
            pass
    else:
        # Not Authorized msg
        bot.sendMessage(uid, 'Sorry, you are not authorized to use this service!')

bot = telepot.Bot(config.apikey)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)