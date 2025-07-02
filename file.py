from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from keep_alive import keep_alive  # В начало файла

keep_alive()  # Перед запуском бота (в main())

TOKEN = "7947462214:AAHZ_K0xNETzLCAAUWHjbc90OJs5Ywgdr8E"  # Замени на реальный токен!

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я тестовый бот. Напиши что-нибудь!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Команды: /start, /help")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Ты написал: {update.message.text}")

def main():
    # Создаем приложение бота
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    print("Бот запущен!")
    application.run_polling()

if __name__ == '__main__':
    main()