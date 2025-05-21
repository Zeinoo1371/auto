import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# فعال‌سازی لاگ برای اشکال‌زدایی
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# توکن ربات
BOT_TOKEN = '8069048315:AAEq5YsgkbYfUPbJDqsq2n0BhketJbgaPJk'

# لیست آیدی گروه‌ها (از نوع عددی)
GROUP_IDS = [
    '@zeinolggg',
    '@zeinol2'
    # گروه‌های بیشتر
]

# هندلر پیام‌های ارسالی در کانال
async def channel_post_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        for group_id in GROUP_IDS:
            try:
                await context.bot.copy_message(
                    chat_id=group_id,
                    from_chat_id=update.channel_post.chat_id,
                    message_id=update.channel_post.message_id
                )
                logger.info(f"پیام با موفقیت به {group_id} ارسال شد.")
            except Exception as e:
                logger.error(f"خطا در ارسال به {group_id}: {e}")

# تابع اصلی اجرای ربات
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, channel_post_handler))

    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
