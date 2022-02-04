

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InlineKeyboardMarkup

from bson.json_util import dumps

from multicolorcaptcha import CaptchaGenerator



from telegram.ext import (

    Updater,

    CommandHandler,

    MessageHandler,

    Filters,

    ConversationHandler,

    CallbackContext,

    PicklePersistence,

)

from telegram.utils import helpersimport telegram



import os



import telegram

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def webhook():
    bot = telegram.Bot(token=os.environ["YOURAPIKEY"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id     = update.effective_chat.id
        text        = update.message.text
        first_name  = update.effective_chat.first_name
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=f"{text} {first_name}")
        bot.message.reply_text(JOINED.replace("REPLACEME", url), reply_markup=ReplyKeyboardMarkup(reply_keyboard))
        return 'ok'
    return 'error'

def index():
    return webhook()
