import random
import telebot
import config
import teams
import socket
# import json

bot = telebot.TeleBot(config.token)
all_teams = [
            teams.liga_bbva,
            teams.seria_a,
            teams.ligue_1,
            teams.bundesliga,
            teams.barclays
            ]
bogma = 426128881
admin = 406626012
pure_random = []
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)

@bot.message_handler(commands=['start', 'help'])
# def cycle(message):
#     for i in list(range(20)):
#         main(message, i)


def main(message):
    # bot.send_message(admin, text='IP: ' + IPAddr)
    liga = random.choice(all_teams)
    team = random.choice(liga)
    # check_team(message, team)
    unique_value = check_team(message, team)
    while unique_value == 'not_unique':
        liga = random.choice(all_teams)
        team = random.choice(liga)
        unique_value = check_team(message, team)
        print(unique_value)
    send_message(message, team, liga)


def check_team(message, team):
    try:
        with open('pure_random/' + str(message.chat.id) + '.txt', 'r') as file:
            text_file = file.read()
            # print(text_file)

            # print(text_file.split('\n'))
            if text_file.count('\n') > 35:
                file.close()
                update_teams_file(message)
                # with open('pure_random/' + str(message.chat.id) + '.txt', 'w') as file:
                #     file.write('')
            if team['team'] in text_file:
                return 'not_unique'
            else:
                return 'unique'
    except:
    #     print('except')
        with open('pure_random/' + str(message.chat.id) + '.txt', 'w') as file:
            file.write('')

def send_message(message, team, liga):
    liga_name = get_liga(liga)
    team_name = team['team']
    team_and_liga = 'Team: ' + team_name + '\nLiga: ' + liga_name + '\n'
    add_pure_random(message, team)
    if message.chat.id != admin:
        if random.choice(range(1, 100)) < 20:
            # bot.send_video(message.chat.id, 'https://c.tenor.com/4fH8zSIuSvcAAAAM/cristiano-ronaldo-soccer.gif')
            fail = open('mp4.mp4', 'rb')
            bot.send_video(message.chat.id, fail)
            bot.send_message(message.chat.id, 'Bonjour гомодрил')
            bot.send_message(message.chat.id, text='Братанчик нахуй это джекпот бери Лягушатников\nСельвупле пидорас')
            bot.send_message(admin, text=message.from_user.first_name + ' должен взять: \n' + 'France')
        else:
            send_logo(team, message)
            bot.send_message(message.chat.id, text=team_and_liga)
            bot.send_message(admin, text=message.from_user.first_name + ' должен взять: \n' + team_and_liga)
        bot.send_message(admin, text=open("pure_random/" + message.chat.id + '.txt'))
    else:
        send_logo(team, message)
        bot.send_message(message.chat.id, text=team_and_liga)
        bot.send_message(admin, text=open("pure_random/" + message.chat.id + '.txt'))


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
        # print(media_url[-4:]) 
        if media_url[-4:] == '.mp4' or media_url[-4:] == '.gif' or media_url[-5:] == '.webm':
            try:
                bot.send_video(message.chat.id, media_url)
            except:
                print('except')
                fail = open('Bztt_L4jfX8.jpg', 'rb')
                bot.send_photo(message.chat.id, fail)
        else:
            bot.send_photo(message.chat.id, media_url)
    else:
        bot.send_message(message.chat.id, text='No logo yet')


def add_pure_random(message, team):
    with open('pure_random/' + str(message.chat.id) + '.txt', 'a') as file:
        
        file.writelines(team['team']+'\n')
    with open('pure_random/' + str(message.chat.id) + '.txt', 'r') as file_read:
        text_file = file_read.read()
        print(text_file.count('\n'))
        print(text_file)


def update_teams_file(message):
    with open('pure_random/' + str(message.chat.id) + '.txt', 'r') as file_read:
        text_file = file_read.read()
        new_text_file = text_file.split('\n')[1:]
    with open('pure_random/' + str(message.chat.id) + '.txt', 'w') as file:
        file.write('\n'.join(new_text_file))
        

bot.polling()
