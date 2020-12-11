from telegram.ext import Updater, MessageHandler, Filters
import requests,json

	
def echo(update, context):
    url = 'https://chatbot-indo.herokuapp.com/get/{}'.format(update.effective_message.text)
    r = requests.get(url)
    j = json.loads(r.text)
    update.effective_message.reply_text(j['msg'])

updater = Updater('1459712147:AAG8Wu-aia1-4Zo1qYuPBMR9EDYMTJT6woQ',
use_context=True)

echo_handler = MessageHandler(Filters.text, echo)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()