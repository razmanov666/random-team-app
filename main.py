import random
import telebot
import config
import teams

bot = telebot.TeleBot(config.token)
all_teams = [teams.liga_bbva, teams.seria_a, teams.ligue_1, teams.bundesliga, teams.barclays]
bogma = 426128881
admin = 406626012

@bot.message_handler(commands=['start', 'help'])
def main(message):
    liga = random.choice(all_teams)
    team = random.choice(liga)
    send_message(message, team, liga)
    

def send_message(message, team, liga):
    liga_name = get_liga(liga)
    team_name = team['team']
    media_url = team['media']
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
    if 'Barcelona' in liga:
        liga_name = 'Liga BBVA'
    elif 'Juventus' in liga:
        liga_name = 'Seria A'
    elif 'PSG' in liga:
        liga_name = 'Ligue 1'
    elif 'Borussia Dortmund' in liga:
        liga_name = 'Bundesliga'
    elif 'Chelsea' in liga:
        liga_name = 'English PL'
    return liga_name


def send_logo(team, message):
    """Send team logo"""
    """Team from France"""
    if team['media'] == '':
        bot.send_video(message.chat.id, 'https://i.pinimg.com/originals/28/9d/17/289d1792fbe86e3a517f4e564117c2c3.gif') 
    else:
        print('True')
    # elif team == 'Monaco':
    #     bot.send_video(message.chat.id, 'https://www.gifservice.fr/img/gif-vignette-small/3c10cec4e948d06c5b6c31536ea7f119/549-2014-sports-soccer-club-france-provence-alpes-cote-dazur-as-monaco-2014.gif')
    
    # elif team == 'Borussia Dortmund':
    #     bot.send_photo(message.chat.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFl3mabt--U-wPh2nMWWggk18FFXFdGSsAKQ&usqp=CAU')
    # elif team == 'Barcelona':
    #     bot.send_video(message.chat.id, 'https://c.tenor.com/HuG2PXbKb98AAAAC/barcelona-fc-barcelona.gif')
    # elif team == 'Real Madrid':
    #     bot.send_video(message.chat.id, 'https://i.gifer.com/HD3f.mp4')


bot.polling()
