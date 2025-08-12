import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")  # Render'da environment variable bo'ladi

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Mover.uz link yuboring.")

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text.startswith("https://mover.uz/watch/"):
        token = text.split("watch/")[1].split("?")[0]
        mp4_url = f"https://v.mover.uz/{token}_m.mp4"
        await update.message.reply_text(mp4_url)
    else:
        await update.message.reply_text("Mover.uz link yuboring!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    app.run_polling()

if __name__ == "__main__":
    main()
