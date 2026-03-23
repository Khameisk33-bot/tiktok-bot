import telebot
import random

TOKEN = "8789719593: AAE445lJa_raU9GFcrf4vDXC1xu gbV2ZLYY"
bot = telebot.TeleBot(TOKEN)

def generate(name):
    name = name.lower().replace(" ", "")
    results = []

    extras = ["x","7","1","v","vx","pro","real"]
    
    for e in extras:
        results.append(f"@{name}{e}")
        results.append(f"@{e}{name}")
        results.append(f"@{name}_{e}")
        results.append(f"@{name}.{e}")

    for i in range(10, 99):
        results.append(f"@{name}{i}")

    random.shuffle(results)
    return results[:50]

@bot.message_handler(func=lambda m: True)
def reply(message):
    name = message.text
    users = generate(name)
    bot.reply_to(message, "\n".join(users))

bot.infinity_polling()
