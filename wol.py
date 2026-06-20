import telebot
from wakeonlan import send_magic_packet
import time

bot = telebot.TeleBot("987654321:ABCdefGhIJKlmNoPQRsTUVwxyZ") # Replace it with your Telegram bot token

MAC = "00:11:22:33:44:55"  # Replace with your MAC address of the computer you want to turn on
ALLOWED_USERS = [123456789]  # Replace with your Telegram ID from which you will send the command

@bot.message_handler(commands=['wol'])
def send_wol(message):
    if message.from_user.id in ALLOWED_USERS:
        send_magic_packet(MAC)
        bot.reply_to(message, "PC starting!")
    else:
        bot.reply_to(message, "You do not have access to this bot.")

# Main loop with auto-restart
while True:
    try:
        bot.polling(non_stop=True, interval=1, timeout=20)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(15)
