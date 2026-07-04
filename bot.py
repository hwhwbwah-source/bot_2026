import telebot

TOKEN = "8950554171:AAHA-t-HFnxBik9NCp4vRaWBZ_Q0zCUkhwM
"
CARD_NUMBER = "2202 2080 0075 6628"

products = {
    "1": {"https://canva.link/h2qinjlvvqfhmqf"},
    
}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    parts = message.text.split()
    product_key = parts[1] if len(parts) > 1 else None
    
    if product_key and product_key in products:
        p = products[product_key]
        bot.send_message(message.chat.id,
            f"🛒 Шаблон {product_key}\n💰 {p['price']} ₽\n💳 Карта: `{CARD_NUMBER}`\n\nОплатите и напишите /check",
            parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "❌ Товара нет. /start 1 или /start 2")

@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.chat.id, "✅ После оплаты я вышлю файл вручную.")

print("Бот запущен!")
bot.infinity_polling()
