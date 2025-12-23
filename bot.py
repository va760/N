from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "8373260222:AAFus4Xn3effyn8vKKDN5nyZrUG3ix9Wips"
user_data = {}  # store UID for users

def start(update: Update, context: CallbackContext):
    update.message.reply_text("សូមបញ្ចូល UID របស់អ្នក:")

def handle_message(update: Update, context: CallbackContext):
    uid = update.message.text.strip()
    if uid.isdigit() and 6 <= len(uid) <= 9:
        user_data[update.message.from_user.id] = uid
        update.message.reply_text(f"✅ UID {uid} ត្រឹមត្រូវ! អ្នកអាចបន្តជាវទំនិញបាន។")
    else:
        update.message.reply_text("❌ UID មិនត្រឹមត្រូវ សូមបញ្ចូលម្ដងទៀត។")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()