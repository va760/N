from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, CallbackContext

# --------- CONFIG ---------
BOT_TOKEN = "8373260222:AAFus4Xn3effyn8vKKDN5nyZrUG3ix9Wips"

# Manual exchange rates
exchange_rates = {
    "usd_khr": 4100,   # 1 USD = 4100 KHR
    "thb_usd": 0.029,  # 1 THB = 0.029 USD
}

# --------- START COMMAND ---------
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("💵 USD → KHR", callback_data="usd_khr")],
        [InlineKeyboardButton("💴 THB → USD", callback_data="thb_usd")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "សូមជ្រើសរើសរូបិយប័ណ្ណដែលចង់បម្លែង:", reply_markup=reply_markup
    )

# --------- BUTTON CALLBACK ---------
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    context.user_data['rate_type'] = query.data
    query.message.reply_text("សូមបញ្ចូលចំនួនដែលចង់បម្លែង:")

# --------- HANDLE AMOUNT INPUT ---------
def handle_amount(update: Update, context: CallbackContext):
    text = update.message.text
    rate_type = context.user_data.get('rate_type')
    if not rate_type:
        update.message.reply_text("សូមជ្រើសរើសរូបិយប័ណ្ណពី Menu ជាមុនសិន!")
        return
    try:
        amount = float(text)
        if rate_type == "usd_khr":
            result = amount * exchange_rates['usd_khr']
            update.message.reply_text(f"{amount} USD = {result:.0f} KHR")
        elif rate_type == "thb_usd":
            result = amount * exchange_rates['thb_usd']
            update.message.reply_text(f"{amount} THB = {result:.2f} USD")
    except ValueError:
        update.message.reply_text("សូមបញ្ចូលលេខត្រឹមត្រូវ!")

# --------- MAIN ---------
def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_amount))

    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()
