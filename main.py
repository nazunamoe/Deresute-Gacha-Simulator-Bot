# -*- coding: utf-8 -*-

import telebot
from telebot import types
from telebot import util

import gacha

bot = telebot.TeleBot("TOKEN")

user = bot.get_me()

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'       : 'Get used to the bot',
    'help'        : 'Gives you information about the available commands',
    'gacha1'      : 'Execute gacha one time',
    'gacha10'     : 'Execute gacha ten times'
}

# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0

# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot.set_update_listener(listener)  # register listener

markup = types.ReplyKeyboardMarkup()
markup.add("Gacha 1 Time","Gacha 10 Times")

@bot.message_handler(commands=['start'])
def send_welcome(message):
		cid = message.chat.id
		bot.send_message(cid, "Choose one", reply_markup=markup)
		userStep[cid] = 1  # set the user to the next step (expecting a reply in the listener now)

# if the user has issued the "/getImage" command, process the answer
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(message):
    cid = message.chat.id
    text = message.text

    # for some reason the 'upload_photo' status isn't quite working (doesn't show at all)
    bot.send_chat_action(cid, 'typing')

    if text == "Gacha 1 Time":  # send the appropriate image based on the reply to the "/getImage" command
        bot.send_message(cid, text= gacha.gachaone())
    elif text == "Gacha 10 Times":
        bot.send_message(cid, text= gacha.gachaten())
    else:
        bot.send_message(cid, "Please, use the predefined keyboard!")
        bot.send_message(cid, "Please try again")

bot.polling()
