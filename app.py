import telebot

# ТВОЙ токен и ID группы
TOKEN = "5771183937:AAHBYjt7maRu20ZuypuBCtAsGBUzrrrilV8"
TARGET_CHAT_ID = -1086767676  # для группы всегда ставим минус

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'sticker', 'voice'])
def forward_message(message):
    try:
        bot.forward_message(TARGET_CHAT_ID, message.chat.id, message.message_id)
    except Exception as e:
        print("Ошибка пересылки:", e)

print("Бот запущен...")
bot.infinity_polling(timeout=60, long_polling_timeout=60)
