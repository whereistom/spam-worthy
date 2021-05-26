import telegram
import datetime
import sys
import requests
from resources import private


bot = telegram.Bot(token=private.api_key)


def send_group(msg, id_list):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    # for x in group_list:
    bot.sendMessage(chat_id=id_list, text=msg, parse_mode='MarkdownV2', disable_web_page_preview='true')


groups_id = private.groups_list_id

# what week number are we in?
week = datetime.date.today().isocalendar()[1]+1
year = datetime.date.today().year

# this week text file content
url = "https://raw.githubusercontent.com/whereistom/spam-worthy/main/" + str(year) + "/" + str(week) + "/" + "text.md" 
data = requests.get(url)


# get markdown message
message = data.text
# message = telegram.utils.helpers.escape_markdown(message, version=2, entity_type="MarkdownV2")
print(message)

# message and list of ids where to send from resources/private
send_group(message, private.test_id)
#raise SystemExit("stop Here")
