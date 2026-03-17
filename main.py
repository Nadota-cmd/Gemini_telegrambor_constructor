import telebot
import requests

# get your token from @BotFather in telegram
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN' 

# get your Gemini API Key here https://aistudio.google.com/app/apikey
KEY = 'YOUR_GEMINI_API_KEY' 

# add Telegram User IDs who can use this bot
# you can get your ID from @userinfobot
ALLOWED_USERS = [12345678, 87654321] 

bot = telebot.TeleBot(TOKEN)

def ask_gemini(prompt, system_instruction):
    # Using Gemini 2.5 Flash
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={KEY}"
    headers = {'Content-Type': 'application/json'}

    payload = {
        "contents": [{
            "parts": [{"text": f"{system_instruction}\n\nUser says: {prompt}"}]
        }]
    }

    try:
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code == 200:
            return res.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"Error Code 63: {res.status_code}"
    except:
        return "Connection lost..."

@bot.message_handler(func=lambda m: m.from_user.id in ALLOWED_USERS)
def handle_message(m):
    #set different roles for different users
    #example:role for the owner
    if m.from_user.id == ALLOWED_USERS[0]:
        role = "bot characteristics."
    #example:role for everyone else
    else:
        role = (
            "also, the bot's characteristics, which you can simply write in ordinary words. "
            "rules:you can also set rules, like 1. Don't use emojis."
        )

    bot.send_chat_action(m.chat.id, 'typing')
    answer = ask_gemini(m.text, role)
    bot.reply_to(m, answer)

print("launch.")
bot.polling(none_stop=True)

# Gemini_telegrambor_constructor
Telegram bot engine powered by Gemini AI. Easy to customize roles, characters, and logic. Works on Termux/Mobile.
