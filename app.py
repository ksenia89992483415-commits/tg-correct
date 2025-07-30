import os
import telebot

TOKEN = os.getenv('-5771183937:AAHBYjt7maRu20ZuypuBCtAsGBUzrrrilV8')
TARGET_CHAT_ID = int(os.getenv('-5771183937'))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    try:
        bot.forward_message(-5771183937, message.chat.id, message.message_id)
    except Exception as e:
        print(f"Ошибка при пересылке: {e}")

print("Бот запущен...")
bot.infinity_polling()
