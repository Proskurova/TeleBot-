import telebot, random
from telebot import types
with open('token.txt', 'r') as f:
    s = f.readlines()
token = s[0]
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    walk_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='4')
    joke_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='5')
    keyboard.add(drink_btn, eat_btn, walk_btn, sleep_btn, joke_btn)
    return keyboard


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == "1":
            img = open('water.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка воды",
                reply_markup=keyboard
            )
            img.close()
        elif call.data == "2":
            img = open('eat.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка еды",
                reply_markup=keyboard
            )
            img.close()
        elif call.data == "3":
            img = open('walk.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Иди гулять",
                reply_markup=keyboard
            )
            img.close()
        elif call.data == "4":
            mp3 = open('detskaja-spjat-ustalye-igrushki.mp3', 'rb')
            bot.send_audio(
                chat_id=call.message.chat.id,
                audio=mp3,
                caption="Включи колыбельную",
                reply_markup=keyboard
            )
            mp3.close()
        elif call.data == "5":
            text = open('joke.txt', 'r', encoding='UTF-8')
            jokes = text.read().split('\n')
            answer = random.choice(jokes)
            bot.send_message(
                chat_id=call.message.chat.id,
                text=answer,
                reply_markup=keyboard
            )
            text.close()


bot.polling(none_stop=True, interval=0)