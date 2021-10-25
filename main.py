import random
import telebot
import config

bot = telebot.TeleBot(config.token)
all_teams = [config.liga_bbva, config.seria_a, config.ligue_1, config.bundesliga, config.barclays]
bogma = 426128881
admin = 406626012

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
    team = random.choice(liga)
    team_and_liga = 'Team: ' + team + '\nLiga: ' + name_liga + '\n'

    # if message.chat.id == bogma or message.chat.id == admin:
    #     print('True')
    #     foto = open('Bztt_L4jfX8.jpg', 'rb')
    #     bot.send_photo(admin, foto)
    #     bot.send_photo(bogma, foto)
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


def send_logo(team, message):
    """Send team logo"""
    """Team from France"""
    if team == 'PSG':
        bot.send_video(message.chat.id, 'https://i.pinimg.com/originals/28/9d/17/289d1792fbe86e3a517f4e564117c2c3.gif') 
    elif team == 'Monaco':
        bot.send_video(message.chat.id, 'https://www.gifservice.fr/img/gif-vignette-small/3c10cec4e948d06c5b6c31536ea7f119/549-2014-sports-soccer-club-france-provence-alpes-cote-dazur-as-monaco-2014.gif')
    # elif team == 'Barcelona':
    #     bot.send_video(message.chat.id, 'https://c.tenor.com/HuG2PXbKb98AAAAC/barcelona-fc-barcelona.gif')
    # elif team == 'Real Madrid':
    #     bot.send_video(message.chat.id, 'https://i.gifer.com/HD3f.gif')
    # elif team == 'Borussia Dortmund':
    #     bot.send_photo(message.chat.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFl3mabt--U-wPh2nMWWggk18FFXFdGSsAKQ&usqp=CAU')
    # elif team == 'Barcelona':
    #     bot.send_video(message.chat.id, 'https://c.tenor.com/HuG2PXbKb98AAAAC/barcelona-fc-barcelona.gif')
    # elif team == 'Real Madrid':
    #     bot.send_video(message.chat.id, 'https://i.gifer.com/HD3f.gif')
    # elif team == 'Borussia Dortmund':
    #     bot.send_photo(message.chat.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFl3mabt--U-wPh2nMWWggk18FFXFdGSsAKQ&usqp=CAU')
    # elif team == 'Barcelona':
    #     bot.send_video(message.chat.id, 'https://c.tenor.com/HuG2PXbKb98AAAAC/barcelona-fc-barcelona.gif')
    # elif team == 'Real Madrid':
    #     bot.send_video(message.chat.id, 'https://i.gifer.com/HD3f.gif')
    # elif team == 'Borussia Dortmund':
    #     bot.send_photo(message.chat.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFl3mabt--U-wPh2nMWWggk18FFXFdGSsAKQ&usqp=CAU')
    # elif team == 'Barcelona':
    #     bot.send_video(message.chat.id, 'https://c.tenor.com/HuG2PXbKb98AAAAC/barcelona-fc-barcelona.gif')
    # elif team == 'Real Madrid':
    #     bot.send_video(message.chat.id, 'https://i.gifer.com/HD3f.gif')
    
    elif team == 'Borussia Dortmund':
        bot.send_photo(message.chat.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFl3mabt--U-wPh2nMWWggk18FFXFdGSsAKQ&usqp=CAU')
    elif team == 'Barcelona':
        bot.send_video(message.chat.id, 'https://c.tenor.com/HuG2PXbKb98AAAAC/barcelona-fc-barcelona.gif')
    elif team == 'Real Madrid':
        bot.send_video(message.chat.id, 'https://i.gifer.com/HD3f.mp4')


bot.polling()
