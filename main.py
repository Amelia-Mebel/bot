import telebot
from telebot import types

bot = telebot.TeleBot('5836443933:AAE_wSBdY7_iI4E4DVmnFYgWDGZUquxfTRs')


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rule = types.KeyboardButton("Rules📖")
    profile = types.KeyboardButton("Profile👤")
    money = types.KeyboardButton("Withdrawal💰")
    veref = types.KeyboardButton("Verification💎")
    work = types.KeyboardButton('Start tasks💼')

    markup.add(rule, profile, money, veref, work)

    bot.send_message(message.chat.id,
                     'Hello, {0.first_name}👋!\n This bot is made for testers🦾.\n Who are ready to receive payments '
                     'for a quick test of app💵.\nPayments are made to MasterCard/Visa cards or ETH wallet💳!'
                     .format(
                         message.from_user, bot.get_me()), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Rules📖':
            bot.send_message(message.chat.id,
                             '1.Each user is responsible for his actions💻\n2.When completing tasks you confirm that '
                             'you agree with the rules of the bot🤖\n3.The bot is an intermediary but not a '
                             'customer🤝\n4.Each issue should be solved only through the administrator👨‍💻\n5.It is '
                             'necessary to perform all tasks💬\n6.When testing the application you agree to the '
                             'customers terms!')
        elif message.text == 'Profile👤':
            cid = message.chat.id
            bot.send_message(message.chat.id, f'👤My Account\n\n➖➖➖➖➖➖➖➖➖➖\n⚠️ Not verified\n➖➖➖➖➖➖➖➖➖➖\n\n💳 '
                                              f'Balance: 0 USD\n📤Processed: 0 USD\n\nYour ID: {cid}')
        elif message.text == 'Withdrawal💰':
            markup = types.InlineKeyboardMarkup(row_width=2)
            visa = types.InlineKeyboardButton("Visa", callback_data='visa')
            master = types.InlineKeyboardButton("MasterCard", callback_data='master')
            btc = types.InlineKeyboardButton("BTC", callback_data='btc')
            eth = types.InlineKeyboardButton("ETH", callback_data='eth')

            markup.add(visa, master, btc, eth)
            bot.send_message(message.chat.id, 'Choose where you want to get paid', reply_markup=markup)

        elif message.text == 'Verification💎':
            bot.send_message(message.chat.id, 'Команда для верефикации')
        elif message.text == 'Start tasks💼':
            bot.send_message(message.chat.id, 'Hendo!!!')
            bot.send_message(message.chat.id, 'Текст задания')
            markup = types.InlineKeyboardMarkup(row_width=2)
            task = types.InlineKeyboardButton("Проверить", callback_data='task')
            markup.add(task)
            bot.send_message(message.chat.id, 'Проверить задание', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            try:
                if call.message:
                    if call.data == 'visa' or call.data == 'master' or call.data == 'btc' or call.data == 'eth':
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='Your balance is '
                                                                                                   'less than 10$')
                    elif call.data == 'task':
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Not confirmed')

            except Exception as e:
                print(repr(e))


bot.polling(none_stop=True)
