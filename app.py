import telebot

TOKEN = "5771183937:AAHBYjt7maRu20ZuypuBCtAsGBUzrrrilV8"
TARGET_CHAT_ID = -1086767676  # ID группы/канала, обязательно с минусом для супергрупп

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    try:
        # Пересылаем сообщение в целевой чат
        bot.forward_message(TARGET_CHAT_ID, message.chat.id, message.message_id)
        print(f"Переслали сообщение {message.message_id} от {message.chat.id}")
    except Exception as e:
        print(f"Ошибка при пересылке: {e}")

print("Бот запущен...")
bot.infinity_polling()
