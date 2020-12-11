from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests,json

def tentang(update, context):
    update.message.reply_text(
        "Hi Bro Namaku Mimi Aku Di Buat Oleh Orang ini @rian1337 ".format(update.message.from_user.first_name))

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
updater.dispatcher.add_handler(CommandHandler('tentang', tentang))
echo_handler = MessageHandler(Filters.text, echo)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
