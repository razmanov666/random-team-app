import random
import telebot
import config

bot = telebot.TeleBot(config.token)
all_teams = [config.liga_bbva, config.seria_a, config.ligue_1, config.bundesliga, config.barclays]


@bot.message_handler(commands=['start', 'help'])
def main(message):
    name_liga = ''
    liga = random.choice(all_teams)
    if 'Barcelona' in liga:
        name_liga = 'Liga BBVA'
    elif 'Juventus' in liga:
        name_liga = 'Seria A'
    elif 'PSG' in liga:
        name_liga = 'Ligue 1'
    elif 'Borussia Dortmund' in liga:
        name_liga = 'Bundesliga'
    elif 'Chelsea' in liga:
        name_liga = 'English PL'
    team_and_liga = 'Team: ' + random.choice(liga) + '\nLiga: ' + name_liga + '\n'
    if message.chat.id != 406626011:
        if random.choice(range(1, 10)) < 3:
            bot.send_message(message.chat.id, text='Братанчик нахуй это джекпот бери ЛЕДЖЕНДС\nСельвупле пидорас')
            bot.send_message(406626012, text= message.from_user.first_name + ' должен взять: \n' + 'Ебаных легенд')
        else:
            bot.send_message(message.chat.id, text=team_and_liga)
            bot.send_message(406626012, text=message.from_user.first_name + ' должен взять: \n' + team_and_liga)
    else :
        bot.send_message(message.chat.id, text=team_and_liga)


bot.polling()
