import random
import telebot
import config
import teams

bot = telebot.TeleBot(config.token)
all_teams = [
            teams.liga_bbva
            # teams.seria_a, 
            # teams.ligue_1, 
            # teams.bundesliga, 
            # teams.barclays
            ]
bogma = 426128881
admin = 406626012

@bot.message_handler(commands=['start', 'help'])
def cycle(message):
    for i in list(range(20)):
        main(message, i)
def main(message, i):
    liga = random.choice(all_teams)
    # team = random.choice(liga)
    team = liga[i]
    send_message(message, team, liga)
    

def send_message(message, team, liga):
    liga_name = get_liga(liga)
    team_name = team['team']
    team_and_liga = 'Team: ' + team_name + '\nLiga: ' + liga_name + '\n'
    if message.chat.id != admin:
        if random.choice(range(1, 10)) < 3:
            bot.send_video(message.chat.id, 'https://c.tenor.com/4fH8zSIuSvcAAAAM/cristiano-ronaldo-soccer.gif')
            bot.send_message(message.chat.id, 'МУЧОС ГРАСИАС АФЕССИОНА SUIIIIIUIU')
            bot.send_message(message.chat.id, text='Братанчик нахуй это джекпот бери ЛЕДЖЕНДС\nСельвупле пидорас')
            bot.send_message(admin, text=message.from_user.first_name + ' должен взять: \n' + 'Ебаных легенд')
        else:
            send_logo(team, message)
            bot.send_message(message.chat.id, text=team_and_liga)
            bot.send_message(admin, text=message.from_user.first_name + ' должен взять: \n' + team_and_liga)
    else:
        send_logo(team, message)
        bot.send_message(message.chat.id, text=team_and_liga)


def get_liga(liga):
    liga_name = ''
    if teams.liga_bbva is liga:
        liga_name = 'Liga BBVA'
    elif teams.seria_a is liga:
        liga_name = 'Seria A'
    elif teams.ligue_1 is liga:
        liga_name = 'Ligue 1'
    elif teams.bundesliga is liga:
        liga_name = 'Bundesliga'
    elif teams.barclays is liga:
        liga_name = 'English PL'
    return liga_name


def send_logo(team, message):
    """Send team logo"""
    """Team from France"""
    media_url = team['media']
    if media_url != '':
        print(media_url[-4:]) 
        if media_url[-4:] == '.mp4' or media_url[-4:] == '.gif':
            try:
                bot.send_video(message.chat.id, media_url)
            except:
                print('except')
                bot.send_photo(message.chat.id, 'Bztt_L4jfX8.jpg')
            finally:
                bot.send_photo(message.chat.id, 'Bztt_L4jfX8.jpg')
        else:
            bot.send_photo(message.chat.id, media_url)
    else:
        bot.send_message(message.chat.id, text='No logo yet')


bot.polling()
