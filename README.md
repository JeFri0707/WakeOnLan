# 📱 Telegram Wake-on-LAN Bot (via Android)

This project allows you to remotely turn on your home PC using a Telegram bot and Wake-on-LAN (WOL) technology.

The unique feature of this solution is that the bot runs on an Android phone, which is always at home and connected to your local Wi-Fi network.

The phone acts as a "mini-server": it receives commands from Telegram and sends a WOL packet to the local network.

---

## ✨ Features
* 🚀 Start your PC with the `/wol` command
* 🔒 Restrict access by user_id
* 🔄 Automatic restart on errors
* 🌐 Works via an Android phone without the need for a public IP or VPS
* 🖥 Ability to manage multiple PCs

---

## ⚙️ How it works
1. The Android phone is always connected to your home Wi-Fi.
2. **Termux**, a Linux emulator, is installed on the phone.
3. A Python script with a Telegram bot is launched in Termux.
4. When you send the `/wol` command in Telegram:
* The bot receives the message via the Telegram cloud.
* Checks if your user_id is in the allowed list.
* Sends a "magic packet" (WOL) to the local network.
* Your PC turns on.

This makes your phone a "bridge" between the internet and your local network.

---

## 🛠 Installation

### 1. Preparing the Environment in Termux
Install Termux on Android, open it, and run the following commands:
```bash
pkg install python nano
pip install pyTelegramBotAPI wakeonlan
```

### 2. Creating the Script File
You won't be able to copy the finished file directly to your phone due to lack of access to Termux's internal file location on Android. Instead, create a new file directly in the Termux console using the `nano` text editor:
```bash
nano wol.py
```
Paste your Python code into the window that opens. To save, press `Ctrl + O`, then `Enter`. To exit the editor, press `Ctrl + X`.

### 3. Configuring the bot 
1. Obtain a Telegram bot token from [@BotFather](https://web.telegram.org/k/#@BotFather). 
2. Find your user_id (e.g., via [@userinfobot](https://web.telegram.org/k/#@userinfobot)).
3. When editing the file, add your user information:
```python
bot = telebot.TeleBot("BOT_TOKEN")
MAC = "YOUR_MAC_ADDRESS"
ALLOWED_USERS = [YOUR_USER_ID]
```

---

## ▶️ Launch

To launch the bot, run the following in the terminal:
```bash
python wol.py
```

---

## 📡 Usage
* Send the `/wol` command to your Telegram bot. * If your `user_id` is in the `ALLOWED_USERS` list, the bot will send a WOL packet and respond:
> **PC starting!**
