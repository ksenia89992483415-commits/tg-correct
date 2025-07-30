TOKEN = '5771183937:AAHBYjt7maRu20ZuypuBCtAsGBUzrrrilV8'  # полученный у @BotFather
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)


GROUP_ID = 1086767676  # Ваш ID группы



# Выдаём Read-only за определённые фразы
@bot.message_handler(content_types=['text'])
def set_ro(message):
    bot.send_message(message.id(-1086767676), 'Какоето сообщение')

print('ЖИВОЙ')
bot.polling()
