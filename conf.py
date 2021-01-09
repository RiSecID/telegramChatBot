from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests,json

def tentang(update, context):
    update.message.reply_text(
        "Hi Bro Namaku Mimi aku diintegrasikan dengan API SimSimi Premium Aku Di Buat Oleh Orang ini @rian1337 [Python 3.8.0] ".format(update.message.from_user.first_name))

def donasi(update, context):
    update.message.reply_text(
        "Hehe senang mendengarnya apabila kamu ingin berdonasi agar bot ini terus aktif setiap saat kamu bisa chat @rian1337".format(update.message.from_user.first_name))

def mulai(update, context):
    update.message.reply_text(
        'Halo {}, Sekarang Kamu Bisa Memulai Chat Denganku'.format(update.message.from_user.first_name))
	
def echo(update, context):
    url = 'https://secureapp.simsimi.com/v1/simsimi/talkset?uid=297390035&av=6.9.3.7&lc=id&cc=ID&tz=Asia%2FJakarta&os=a&ak=Nsh1x94iNA2oftvixJMmTj1awEk%3D&message_sentence={}&normalProb=8&isFilter=1&talkCnt=8&talkCntTotal=8&reqFilter=1&session=MMWBpntzK2hS64aX7SuhQHTcsHCrVftmwJBk7cGd3ViCyVTFx4ywxuEvvTHnQWrt9ENooUhdQXaD6XrDuTyGbSv2&triggerKeywords=%5B%5D'.format(update.effective_message.text)
    r = requests.get(url)
    data = json.loads(r.text)
    # update.effective_message.reply_text(data['simsimi_talk_set']['answers'][0]['sentence'])
    update.effective_message.reply_text("Bot mati dulu ya gan")

updater = Updater('1459712147:AAGIk8Q6DNyl-HbgtsbuP7u2AnItfIESqJE',
use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', mulai))
updater.dispatcher.add_handler(CommandHandler('tentang', tentang))
updater.dispatcher.add_handler(CommandHandler('donasi', donasi))
echo_handler = MessageHandler(Filters.text, echo)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
