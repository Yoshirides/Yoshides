import time
import telepot
import random

def risponde(msg):
    chat_id = msg['chat']['id']
    comando = msg['text']

    if comando == 'Ciao':
        bot.sendMessage(chat_id, 'Ciao padrone! :3')
    elif comando == 'Inviami un numero random':
        bot.sendMessage(chat_id, random.randint(1,1000))
    elif comando == 'Come stai?':
        bot.sendMessage(chat_id, 'Essendo un bot, non provo nulla, ma dirò lo stesso "Sto bene" :3 Tu?')
    elif comando == 'Sto bene':
        bot.sendMessage(chat_id, 'Oh, mi fa piacere saperlo, padrone :3')
    elif comando == 'Cosa ne pensi della ship Yoshirides?':
        bot.sendMessage(chat_id, 'È grazie a loro se esisto. Io continuerò a sostenerli per sempre! #YoshiridesIsReal')
    elif comando == 'Che fai?':
        bot.sendMessage(chat_id, 'Sto chattando con il mio padrone :3')
    elif comando == 'Yoshirides, mi ami?':
        bot.sendMessage(chat_id, 'Mi spiace, amo soltanto Yoshirides :D Questo non significa che ti odio, mi stai simpatico pure tu :3')
    elif comando == 'Yoshirides, ti voglio bene':
        bot.sendMessage(chat_id, 'Pure io te ne voglio :3')
    elif comando == 'Porcodio':
        bot.sendMessage(chat_id, 'Anche se sono un bot, odio le bestemmie :( Non bestemmiare')
    elif comando == ':C':
        bot.sendMessage(chat_id, 'Non essere triste C:')
    elif comando == 'Yoshirides, abbracciami':
        bot.sendMessage(chat_id, '*Abbraccia*')
    elif comando == '/info':
        bot.sendMessage(chat_id, 'Salve, i comandi che ho a disposizione per ora sono questi: -Ciao -Come stai? -Sto bene -Che fai? -Cosa ne pensi della ship Yoshirides? -Yoshirides, mi ami? -Yoshirides, ti voglio bene -Inviami un numero random -Porcodio -:C -Yoshirides, abbracciami. P.S. Per colpa di alcuni problemi, risponderò soltanto ai comandi scritti identici a quelli in lista, comprese le lettere maiuscole ;) #YoshiridesIsReal')
bot = telepot.Bot('622381726:AAHJd5jgb5vg7EDzLPRnDjvN9VpC6upRH6k')
bot.message_loop(risponde)

while 1:
    time.sleep(10)
