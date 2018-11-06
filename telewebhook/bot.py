import os
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None
PREFIX = 'https://www.instagram.com/p/'
BOT_TOKEN = os.environ.get('BOT_TOKEN')

def main():
    global update_id
    bot = telegram.Bot(BOT_TOKEN)

    print(bot.first_name)
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1


def echo(bot):
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:
            print(update.message.text)
            update.message.reply_text(update.message.text)

if __name__ == '__main__':
    main()
