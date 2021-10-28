import random
liga_bbva = [   {'team':'Barcelona', 'media': 'https://c.tenor.com/HuG2PXbKb98AAAAC/barcelona-fc-barcelona.gif'},
                {'team':'Real Madrid', 'media': 'https://i.gifer.com/HD3f.mp4'},
                {'team':'Alavés', 'media': 'https://upload.wikimedia.org/wikipedia/ru/thumb/e/e7/Deportivo_Alaves_logo_%282020%29.png/200px-Deportivo_Alaves_logo_%282020%29.png'},
                {'team':'Athletic Bilbao', 'media': 'https://phoneky.co.uk/thumbs/screensavers/down/sports/bilbao_psxcmu82.gif'},
                {'team':'Atlético Madrid', 'media': 'https://img1.picmix.com/output/pic/normal/8/8/6/2/6102688_01eec.gif'},
                {'team':'Cádiz', 'media': 'https://i.pinimg.com/originals/11/bb/61/11bb613328642e798568fab47d1fef01.gif'},
                {'team':'Celta Vigo', 'media': 'https://c.tenor.com/uj-SfMZ63tEAAAAd/celta-de-vigo.gif'},
                {'team':'Eibar', 'media': 'https://c.tenor.com/kCuz2afeA5wAAAAi/eibar-sd-eibar.gif'},
                {'team':'Elche', 'media': 'https://images.myguide-cdn.com/alicante/companies/elche-fc/large/elche-fc-689131.jpg'},
                {'team':'Getafe', 'media': 'https://c.tenor.com/91dYAas8UfAAAAAd/bordal%C3%A1s-getafe-sorpresa.gif'},
                {'team':'Granada', 'media': 'http://4.bp.blogspot.com/-nTCBLK__krw/USMvAtavVnI/AAAAAAAAACk/d4LjDOdI7TI/s320/escudo+granada+para+colorear.gif'},
                {'team':'Huesca', 'media': 'https://besthqwallpapers.com/Uploads/12-12-2019/115179/thumb2-huesca-fc-golden-logo-la-liga-2-red-metal-background-football.jpg'},
                {'team':'Levante', 'media': ''},
                {'team':'Osasuna', 'media': ''},
                {'team':'Real Betis', 'media':  ''},
                {'team':'Real Sociedad', 'media':  ''},
                {'team':'Sevilla', 'media': ''},
                {'team':'Valencia', 'media': ''},
                {'team':'Valladolid', 'media': ''},
                {'team':'Villarreal', 'media': ''}]

seria_a = [ {'team': 'Juventus', 'media': ''},
            {'team': 'AC Milan', 'media': ''},
            {'team': 'Atalanta', 'media': ''},
            {'team': 'Benevento', 'media': ''},
            {'team': 'Bologna', 'media': ''},
            {'team': 'Cagliari', 'media': ''},
            {'team': 'Crotone', 'media': ''},
            {'team': 'Fiorentina', 'media': ''},
            {'team': 'Genoa', 'media': ''},
            {'team': 'Hellas Verona', 'media': ''},
            {'team': 'Internazionale', 'media': ''},
            {'team': 'Lazio', 'media': ''},
            {'team': 'Napoli', 'media': ''},
            {'team': 'Parma', 'media': ''},
            {'team': 'Roma', 'media': ''},
            {'team': 'Sampdoria', 'media': ''},
            {'team': 'Sassuolo', 'media': ''},
            {'team': 'Spezia', 'media': ''},
            {'team': 'Torino', 'media': ''},
            {'team': 'Udinese', 'media': ''}]

ligue_1 = [ {'team': 'PSG', 'media': 'https://i.pinimg.com/originals/28/9d/17/289d1792fbe86e3a517f4e564117c2c3.gif'},
            {'team': 'Monaco', 'media': 'https://www.gifservice.fr/img/gif-vignette-small/3c10cec4e948d06c5b6c31536ea7f119/549-2014-sports-soccer-club-france-provence-alpes-cote-dazur-as-monaco-2014.gif'},
            {'team': 'Angers', 'media': ''},
            {'team': 'Bordeaux', 'media': ''},
            {'team': 'Brest', 'media': ''},
            {'team': 'Dijon', 'media': ''},
            {'team': 'Lens', 'media': ''},
            {'team': 'Lille', 'media': ''},
            {'team': 'Lorient', 'media': ''},
            {'team': 'Lyon', 'media': ''},
            {'team': 'Marseille', 'media': ''},
            {'team': 'Metz', 'media': ''},
            {'team': 'Montpellier', 'media': ''},
            {'team': 'Nantes', 'media': ''},
            {'team': 'Nice', 'media': ''},
            {'team': 'Nîmes', 'media': ''},
            {'team': 'Reims', 'media': ''},
            {'team': 'Rennes', 'media': ''},
            {'team': 'Saint-Étienne', 'media': ''},
            {'team': 'Strasbourg', 'media': ''}]

bundesliga = [  {'team': 'Borussia Dortmund', 'media': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFl3mabt--U-wPh2nMWWggk18FFXFdGSsAKQ&usqp=CAU'},
                {'team': 'Bayern Munich', 'media': ''},
                {'team': 'FC Augsburg', 'media': ''},
                {'team': 'Hertha BSC', 'media': ''},
                {'team': 'Union Berlin', 'media': ''},
                {'team': 'Arminia Bielefeld', 'media': ''},
                {'team': 'Werder Bremen', 'media': ''},
                {'team': 'Eintracht Frankfurt', 'media': ''},
                {'team': 'SC Freiburg', 'media': ''},
                {'team': '1899 Hoffenheim', 'media': ''},
                {'team': '1. FC Köln', 'media': ''},
                {'team': 'RB Leipzig', 'media': ''},
                {'team': 'Bayer Leverkusen', 'media': ''},
                {'team': 'Mainz 05', 'media': ''},
                {'team': 'Borussia Mönchengladbach', 'media': ''},
                {'team': 'Schalke 04', 'media': ''},
                {'team': 'VfB Stuttgart', 'media': ''},
                {'team': 'VfL Wolfsburg', 'media': ''}]

barclays = [{'team': 'Chelsea', 'media': ''},
            {'team': 'Manchester United', 'media': ''},
            {'team': 'Arsenal', 'media': ''},
            {'team': 'Aston Villa', 'media': ''},
            {'team': 'Brighton & Hove Albion', 'media': ''},
            {'team': 'Burnley', 'media': ''},
            {'team': 'Crystal Palace', 'media': ''},
            {'team': 'Everton', 'media': ''},
            {'team': 'Fulham', 'media': ''},
            {'team': 'Leeds United', 'media': ''},
            {'team': 'Leicester City', 'media': ''},
            {'team': 'Liverpool', 'media': ''},
            {'team': 'Manchester City', 'media': ''},
            {'team': 'Newcastle United', 'media': ''},
            {'team': 'Sheffield United', 'media': ''},
            {'team': 'Southampton', 'media': ''},
            {'team': 'Tottenham Hotspur', 'media': ''},
            {'team': 'West Bromwich Albion', 'media': ''},
            {'team': 'West Ham United', 'media': ''},
            {'team': 'Wolverhampton Wanderers', 'media': ''}]
# team = random.choice(liga_bbva)

# print(liga_bbva[2])