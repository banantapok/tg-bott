from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Словарь для хранения учетных данных пользователей
user_credentials = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Введите команду /register для регистрации или /login для входа.')

def register(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Введите ваш ID и пароль через пробел.')

def save_credentials(update: Update, context: CallbackContext) -> None:
    user_data = update.message.text.split()
    if len(user_data) != 3:
        update.message.reply_text('Пожалуйста, введите команду в формате: /register ID пароль.')
        return
    
    command, user_id, password = user_data
    user_credentials[user_id] = password
    update.message.reply_text('Регистрация прошла успешно!')

def login(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Введите ваш ID и пароль через пробел.')

def check_credentials(update: Update, context: CallbackContext) -> None:
    user_data = update.message.text.split()
    if len(user_data) != 3:
        update.message.reply_text('Пожалуйста, введите команду в формате: /login ID пароль.')
        return
    
    command, user_id, password = user_data
    if user_id in user_credentials and user_credentials[user_id] == password:
        update.message.reply_text('Вы успешно вошли в систему!')
    else:
        update.message.reply_text('Неправильный ID или пароль.')

def main() -> None:
    # Введите токен, который вы получили от BotFather
    updater = Updater("7021864343:AAEjimPLRz9koQNYdsG7Sunh0fghOnY9CFg")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("register", register))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex(r'^/register'), save_credentials))
    dispatcher.add_handler(CommandHandler("login", login))
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.regex(r'^/login'), check_credentials))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
