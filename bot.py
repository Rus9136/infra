import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "7571223687:AAGrF5xW-rqzdcqq2mnFIou40yuNVgK9Lhw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    web_app = WebAppInfo(url="https://8e40-149-27-215-155.ngrok-free.app/index.html")
    #web_app = WebAppInfo(url="https: // 8e40 - 149 - 27 - 215 - 155.ngrok-free.app/index.html") # заменишь на свой URL
    markup.add(InlineKeyboardButton(text="Открыть мини-апп", web_app=web_app))
    bot.send_message(message.chat.id, "Нажми на кнопку ниже, чтобы открыть мини-апп", reply_markup=markup)

@bot.message_handler(content_types=["web_app_data"])
def handle_web_app(message):
    bot.send_message(message.chat.id, f"Ты отправил из мини-аппа: {message.web_app_data.data}")

bot.polling()