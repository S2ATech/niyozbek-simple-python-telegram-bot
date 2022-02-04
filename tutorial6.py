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



    if(bot.message.text == 'Hi'):

      bot.sendMessage(chat_id=chat_id, text=f"Hello {first_name}!")
      
      return 'ok'

    return 'error'

def index():

    return webhook()
