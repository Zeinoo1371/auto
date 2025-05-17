import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# بارگذاری متغیرهای محیطی
load_dotenv()

# توکن و آیدی‌ها
BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHANNEL_ID = int(os.getenv("SOURCE_CHANNEL_ID"))
GROUP_IDS = [int(chat_id.strip()) for chat_id in os.getenv("GROUP_IDS").split(",")]

def forward_post(update: Update, context: CallbackContext):
    if update.effective_chat.id == SOURCE_CHANNEL_ID:
        for group_id in GROUP_IDS:
            try:
                context.bot.forward_message(
                    chat_id=group_id,
                    from_chat_id=update.effective_chat.id,
                    message_id=update.message.message_id
                )
                print(f"پیام به گروه {group_id} ارسال شد.")
            except Exception as e:
                print(f"خطا در ارسال پیام به گروه {group_id}: {e}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.chat(chat_id=SOURCE_CHANNEL_ID), forward_post))

    print("ربات فعال است...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
