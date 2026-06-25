import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.environ.get('TOKEN') or os.environ.get('BOT_TOKEN')

if not TOKEN:
    raise ValueError("❌ توکن بات در Environment Variables تنظیم نشده!")

app = ApplicationBuilder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text(
        "⚡ **WA.io Token**\n\n"
        "🪙 ۱۰ میلیارد توکن | BNB Smart Chain\n"
        "📈 رشد سریع | ماینینگ ۲۴/۷\n"
        "🌍 ارجاع و پاداش\n\n"
        "🔗 وبسایت: https://wa.io\n"
        "💬 پشتیبانی: @WAioSupport"
    )

async def help_command(update, context):
    await update.message.reply_text(
        "برای شروع ماینینگ به سایت https://wa.io مراجعه کنید.\n"
        "سوالات خود را به @WAioSupport بفرستید."
    )

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

if __name__ == "__main__":
    print("🚀 WA.io Bot started successfully...")
    app.run_polling(drop_pending_updates=True)
