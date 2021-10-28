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
                {'team':'Levante', 'media': 'https://c.tenor.com/b0XtzaeK6xgAAAAd/txus-bixquert-levante-ud.gif'},
                {'team':'Osasuna', 'media': 'https://c.tenor.com/_5n1MTps7fQAAAAd/osasuna-sergioherrera.gif'},
                {'team':'Real Betis', 'media':  'https://c.tenor.com/5IY1_slrbA8AAAAj/alex-moreno-real-betis.gif'},
                {'team':'Real Sociedad', 'media':  'https://c.tenor.com/ntrvlpTVEbQAAAAC/imanol-alguacil-imanol.gif'},
                {'team':'Sevilla', 'media': 'https://amazfitwatchfaces.com/storage/gtr/img/1617104197_945c22e88f.gif'},
                {'team':'Valencia', 'media': 'https://c.tenor.com/opBK_g5gKnUAAAAC/valencia-logo.gif'},
                {'team':'Valladolid', 'media': 'https://amazfitwatchfaces.com/storage/bip/img/5c224e471fc81_25122018.gif'},
                {'team':'Villarreal', 'media': 'https://c.tenor.com/jy4W_x2JeacAAAAi/villarreal-la.gif'}]

seria_a = [ {'team': 'Juventus', 'media': 'https://c.tenor.com/2vMBsfOaJwgAAAAi/cristiano-ronaldo-ronaldo.gif'},
            {'team': 'AC Milan', 'media': 'https://c.tenor.com/49IPKC1sGSIAAAAM/ibra.gif'},
            {'team': 'Atalanta', 'media': 'https://c.tenor.com/ISG8NxOXelsAAAAd/atalanta-fc-robin-gosens.gif'},
            {'team': 'Benevento', 'media': 'https://c.tenor.com/7BvifRcWAx0AAAAM/gaich-adolfo-gaich.gif'},
            {'team': 'Bologna', 'media': 'https://www.periodicodaily.com/wp-content/uploads/2017/12/Bologna_FC_animata_2.gif'},
            {'team': 'Cagliari', 'media': 'https://c.tenor.com/zCCxEIbgOeYAAAAM/calcio-buongiorno-cagliari-flex.gif'},
            {'team': 'Crotone', 'media': 'https://c.tenor.com/wPmzvpXIKRYAAAAM/cisim-crotone.gif'},
            {'team': 'Fiorentina', 'media': 'https://c.tenor.com/rjXlV-xV2UUAAAAC/berkay-fiorentina.gif'},
            {'team': 'Genoa', 'media': 'https://genoa1893.altervista.org/images/gif/genoagruppo.gif'},
            {'team': 'Hellas Verona', 'media': 'https://c.tenor.com/9JXMiSpk3DkAAAAM/strip-verona.gif'},
            {'team': 'Internazionale', 'media': 'https://c.tenor.com/pz7SvVhGVS4AAAAM/inter-karmaleague.gif'},
            {'team': 'Lazio', 'media': 'https://c.tenor.com/Tap5tpRC6HkAAAAM/lazio-sslazio.gif'},
            {'team': 'Napoli', 'media': 'https://img1.picmix.com/output/pic/normal/1/2/0/8/6158021_d3804.gif'},
            {'team': 'Parma', 'media': 'https://media1.giphy.com/media/l41Ya5G9Ou6qHHGw0/giphy-downsized.gif'},
            {'team': 'Roma', 'media': 'https://c.tenor.com/mG26RF8wN-QAAAAM/asroma-as-roma-squadra-logo-wolf.gif'},
            {'team': 'Sampdoria', 'media': 'https://c.tenor.com/P7NDPiAqpXIAAAAS/berkay-fiorentina.gif'},
            {'team': 'Sassuolo', 'media': 'https://c.tenor.com/dN3at7tuutMAAAAd/sassuolo-sassuolo-calcio.gif'},
            {'team': 'Spezia', 'media': 'https://besthqwallpapers.com/Uploads/29-6-2018/57687/thumb2-spezia-calcio-4k-logo-geometric-art-serie-b.jpg'},
            {'team': 'Torino', 'media': 'https://c.tenor.com/HWzo-o2x43EAAAAM/il-gallo-belotti.gif'},
            {'team': 'Udinese', 'media': 'https://cdn.dribbble.com/users/659111/screenshots/6511710/udinese_artboard_1_copyv_2_2_artboard_1_copyv_2_2_1x.png?compress=1&resize=400x300'}]

ligue_1 = [ {'team': 'PSG', 'media': 'https://i.pinimg.com/originals/28/9d/17/289d1792fbe86e3a517f4e564117c2c3.gif'},
            {'team': 'Monaco', 'media': 'https://www.gifservice.fr/img/gif-vignette-small/3c10cec4e948d06c5b6c31536ea7f119/549-2014-sports-soccer-club-france-provence-alpes-cote-dazur-as-monaco-2014.gif'},
            {'team': 'Angers', 'media': 'https://monophy.com/media/8F0RHILk9b96HEgmpl/monophy.gif'},
            {'team': 'Bordeaux', 'media': 'https://besthqwallpapers.com/Uploads/1-12-2018/73004/thumb2-fc-girondins-bordeaux-4k-logo-creative-art-blue-white-checkered-flag.jpg'},
            {'team': 'Brest', 'media': 'https://c.tenor.com/ypcSg4pzmH0AAAAC/sb29-brest.gif'},
            {'team': 'Dijon', 'media': 'https://c.tenor.com/ILylGPSESP4AAAAS/brice-jovial-dfco.gif'},
            {'team': 'Lens', 'media': 'https://c.tenor.com/71PzPaxe1R4AAAAC/rc-lens-racing-club-de-lens.gif'},
            {'team': 'Lille', 'media': 'https://c.tenor.com/BdlF31bv2fUAAAAS/losc-lille-osc.gif'},
            {'team': 'Lorient', 'media': 'https://c.tenor.com/mjNRWPLc1Z0AAAAS/fc-lorient-lorient.gif'},
            {'team': 'Lyon', 'media': 'https://www.gifimili.com/gif/2019/02/olympique-lyonnais-logo-eclair.gif'},
            {'team': 'Marseille', 'media': 'https://c.tenor.com/Ik2dPd4VgPcAAAAS/allez-lom-olympique-de-marseille.gif'},
            {'team': 'Metz', 'media': 'https://besthqwallpapers.com/Uploads/30-4-2020/130638/thumb2-fc-metz-glitter-logo-ligue-1-purple-white-checkered-background-soccer.jpg'},
            {'team': 'Montpellier', 'media': 'https://c.tenor.com/4POCVOTfH6cAAAAS/montpellier.gif'},
            {'team': 'Nantes', 'media': 'http://www.animated-gifs.fr/category_emoticons/smilies-sports-galleries/73734310.gif'},
            {'team': 'Nice', 'media': 'https://besthqwallpapers.com/Uploads/29-10-2019/109646/thumb2-ogc-nice-golden-logo-ligue-1-red-metal-background-football.jpg'},
            {'team': 'Nîmes', 'media': 'https://c.tenor.com/dm-hhdbpvGQAAAAS/nimes-maison-carr%C3%A9e.gif'},
            {'team': 'Reims', 'media': 'https://upload.wikimedia.org/wikipedia/fr/thumb/e/ec/Stade_de_Reims.svg/369px-Stade_de_Reims.svg.png'},
            {'team': 'Rennes', 'media': 'https://c.tenor.com/haX95DGXtsAAAAAd/stade-rennais.gif'},
            {'team': 'Saint-Étienne', 'media': 'http://carnus.c.a.pic.centerblog.net/4c3dc5f2.gif'},
            {'team': 'Strasbourg', 'media': 'https://c.tenor.com/dMdu4O5Cpc4AAAAS/strasbourg.gif'}]

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