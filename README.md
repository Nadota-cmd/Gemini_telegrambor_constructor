🤖 Gemini AI Telegram Bot Constructor

Universal engine for creating your own AI Telegram Bot with custom personalities. Works perfectly on Termux (Android) and PC.

🚀 Quick Start Guide / Быстрый старт

Follow these 4 steps to get your bot running:

1. 🔑 Get Telegram Token (BotFather)
- Open [Telegram](https://t.me/BotFather) and find **@BotFather**.
- Send `/newbot` command.
- Give your bot a name and a username.
- **Copy the API Token** and save it.

2. 🧠 Get Gemini API Key (Google AI)
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
- Create a new API Key (Gemini 2.5 Flash is recommended).
- **Copy the Key**.

3. 🆔 Find your Telegram ID
- Open [Telegram](https://t.me/userinfobot) and find **@userinfobot**.
- Send any message to it.
- It will give you your **ID** (a long number like `6651958858`). Use this in the `ALLOWED_USERS` list in the code.

4. 📱 Setup Termux (Android)
Open your Termux and run these commands:
```bash
pkg update && pkg upgrade
pkg install python
pip install pyTelegramBotAPI requests

