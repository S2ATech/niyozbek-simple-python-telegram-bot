from flask import Flask, render_template, request

from  dotenv import load_dotenv

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

import os

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                     level=logging.INFO)




import telegram

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def webhook():

    bot = telegram.Bot(token=os.environ["YOURAPIKEY"],use_context=True)


    if request.method == "POST":

        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id     = update.effective_chat.id

        text        = update.message.text

        first_name  = update.effective_chat.first_name

        # Reply with the same message

        bot.sendMessage(chat_id=chat_id, text=f"{text} {first_name}")
dispatcher = bot.dispatcher

#not needed



def start(bot, context):

    bot.sendMessage(chat_id=chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

def stop(botb, context):

    context.bot.send_message(chat_id=bot.effective_chat.id, text="Please talk to me, do not stop me!")

stop_handler = CommandHandler('stop', stop)

dispatcher.add_handler(stop_handler)

def echo(bot, context):

    if(bot.message.text == 'Hi'):

        context.bot.send_message(chat_id=chat_id, text=f"Hi {bot.effective_chat.first_name}!")

    else:

        context.bot.send_message(chat_id=chat_id, text=bot.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(echo_handler)

dispatcher = bot.dispatcher

#not needed

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                     level=logging.INFO)

def start(bot, context):

    context.bot.send_message(chat_id=bot.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

def stop(botb, context):

    context.bot.sendMessage(chat_id=bot.effective_chat.id, text="Please talk to me, do not stop me!")

stop_handler = CommandHandler('stop', stop)

dispatcher.add_handler(stop_handler)

def echo(bot, context):

    if(bot.message.text == 'Hi'):

        context.bot.sendMessage(chat_id=chat_id, text=f"Hi {bot.effective_chat.first_name}!")

    else:

        context.bot.sendMessage(chat_id=chat_id, text=bot.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(echo_handler)


        return 'ok'

    return 'error'

def index():

    return webhook()
