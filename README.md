🇺🇲 : 🤖 Gemini AI Telegram Bot Constructor

Universal engine for creating your own AI Telegram Bot with custom personalities. Works perfectly on Termux (Android) and PC.

🚀 Quick Start Guide 

Follow these 4 steps to get your bot running:

1. 🔑 Get Telegram Token (BotFather)
- Open [Telegram](https://t.me/BotFather) and find **@BotFather**.
- Create a bot in the menu
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
pip install pyTelegramBotAPI requests ```

🇷🇺 : 🤖 Gemini ИИ телеграмм бот конструктор 

Универсальный движок для создания собственного Telegram-бота с искусственным интеллектом и настраиваемыми параметрами. Отлично работает в Termux (Android) и на ПК.

🚀 Быстрый старт за 5 минут:

1. 🔑 Создаем бота (BotFather)
- Зайди в [@BotFather](https://t.me/BotFather) в Telegram.
- Создай бота в меню
- Придумай имя и юзернейм для бота.
- **Скопируй API Token** (длинная строка с цифрами и буквами). Это твой ключ управления.

2. 🧠 Получаем мозги (Google API Key)
- Перейди в [Google AI Studio](https://aistudio.google.com/app/apikey)
- Создай новый API Key (выбирай модель Gemini 2.5 Flash — она самая быстрая и бесплатная).
- **Скопируй этот ключ**. Без него ИИ не будет отвечать.

3. 🆔 Узнаем свой ID
- Чтобы бот не слушался каждого встречного, найди [@userinfobot](https://t.me/userinfobot).
- Напиши ему любое сообщение, и он выдаст твой **ID** (цифры типа `6651958858`). 
- Вставь эти цифры в список `ALLOWED_USERS` в файле `main.py`.

4. 📱 Запуск в Termux (на телефоне)
Открой Termux и по очереди вводи эти команды:
```bash
pkg update && pkg upgrade
pkg install python
pip install pyTelegramBotAPI requests


