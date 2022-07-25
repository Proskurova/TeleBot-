# В этот телеграмм бот напиши любое слово, и он найдет его значение на Wikipedia
import telebot, wikipedia, re
with open('token.txt', 'r') as f:
    s = f.read().split('\n')
token = s[1]
bot = telebot.TeleBot(token)
wikipedia.set_lang("ru")


def clean_text(a):
    try:
        ny = wikipedia.page(a)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if len((x.strip())) > 3:
                   wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, clean_text(message.text))


bot.polling(none_stop=True, interval=0)