import telebot
import random
from telebot import types

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Gacha bot started")

@bot.message_handler(commands=['gacha'])
def send_welcome(message):
	bot.reply_to(message, gachaone())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

def gachaone():
	temp = random.randrange(1,1000)
	if temp <= 30: return "SSRare"
	elif temp <= 130: return "SRare"
	else: return "Rare"

bot.polling()