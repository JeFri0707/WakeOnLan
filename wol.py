import telebot
from wakeonlan import send_magic_packet
import time

bot = telebot.TeleBot("987654321:ABCdefGhIJKlmNoPQRsTUVwxyZ") # замените на свой токен бота в Telegram

MAC = "00:11:22:33:44:55"  # замените на свой MAC адрес компьютера, который нужно включать
ALLOWED_USERS = [123456789]  # замените на свой Telegram ID с которого будете отправлять команду

@bot.message_handler(commands=['wol'])
def send_wol(message):
    if message.from_user.id in ALLOWED_USERS:
        send_magic_packet(MAC)
        bot.reply_to(message, "ПК запускается!")
    else:
        bot.reply_to(message, "У Вас нету доступа к этому боту.")

# Основной цикл с автоперезапуском
while True:
    try:
        bot.polling(non_stop=True, interval=1, timeout=20)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(15)
