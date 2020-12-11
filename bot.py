from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests,json

def mulai(update, context):
    update.message.reply_text(
        'Halo, {}, Sekarang Kamu Bisa Memulai Chat Denganku'.format(update.message.from_user.first_name))
	
def echo(update, context):
    url = 'https://chatbot-indo.herokuapp.com/get/{}'.format(update.effective_message.text)
    r = requests.get(url)
    j = json.loads(r.text)
    update.effective_message.reply_text(j['msg'])

updater = Updater('1459712147:AAG8Wu-aia1-4Zo1qYuPBMR9EDYMTJT6woQ',
use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', mulai))
echo_handler = MessageHandler(Filters.text, echo)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
