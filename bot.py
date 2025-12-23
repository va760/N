from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import requests

API_TOKEN = "8373260222:AAFus4Xn3effyn8vKKDN5nyZrUG3ix9Wips"

# Example: use TikTok unofficial API or public endpoint
def get_tiktok_stats(url):
    api_url = f"https://api.tiktokv.com/your_endpoint?url={url}"  # placeholder
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return {
            "views": data.get("stats", {}).get("playCount", "N/A"),
            "likes": data.get("stats", {}).get("diggCount", "N/A"),
            "comments": data.get("stats", {}).get("commentCount", "N/A"),
            "shares": data.get("stats", {}).get("shareCount", "N/A")
        }
    else:
        return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("សួស្តី! ផ្ញើ TikTok link របស់អ្នកដើម្បី track stats 📈")

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    stats = get_tiktok_stats(url)
    if stats:
        msg = f"📊 TikTok Stats:\nViews: {stats['views']}\nLikes: {stats['likes']}\nComments: {stats['comments']}\nShares: {stats['shares']}"
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("❌ មិនអាចទាញ stats បាន, សូមព្យាយាមម្តងទៀត")

app = ApplicationBuilder().token(API_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

app.run_polling()
