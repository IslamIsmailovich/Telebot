import telebot
import time
bot = telebot.TeleBot("")
responses = {}
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    responses[user_id] = []
    bot.send_message(message.chat.id, "Привет! как ты! ответишь на вопрос ?")
    time.sleep(1)
        ask_question(message, user_id)

@bot.message_handler(func=lambda message: True)
def handle_message(message,user_id):
    if "хорошо" in message.text.lower() or "отлично" in message.text.lower():
        responses[user_id].append(answer)
        bot.send_message(message.chat.id, "Рад слышать! как прошел день? ")
    elif "отлично" in message.text.lower() or "не очень" in message.text.lower():
        bot.send_message(message.chat.id, "даа, у каждого по разному !   А о чем ты мечтаешь? ")
    else:
        bot.send_message(message.chat.id, "Класс на этом всё удачного дня. ")

bot.polling()
