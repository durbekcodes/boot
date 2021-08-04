import telebot
from telebot import types
#Dasturchi @Azizbek_K
bot = telebot.TeleBot('1857847199:AAEqyroqU3480MJDfYVBTXQK3iJtuIoogJk')

@bot.message_handler(func=lambda m: True)
def welcome(m):
    idd = m.from_user.id
    if m.text == '/start' :
        key = types.ReplyKeyboardMarkup(True)
        key.row('salom', 'Men haqimda')
        text = 'Assalomu alaykum {} {}.'.format(m.from_user.first_name, m.from_user.last_name);
        bot.send_message(idd, text, reply_markup=key)  
    if m.text == 'salom' or m.text == '/hi':
        text = 'Sizga ham salom';
        bot.send_message(idd, text)
    if m.text == 'Men haqimda' or m.text == '/me':
        text = 'Men @Azizbek_K tominidan yozildim';
        bot.send_message(idd, text)

bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
