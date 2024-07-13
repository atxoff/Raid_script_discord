import os
import subprocess
import colorama
from termcolor import colored

# Initialisation de colorama
colorama.init()

# ASCII Art
ascii_art = '''
__________        .__    .___   __________        __    ___.                   __          
\______   \_____  |__| __| _/   \______   \ _____/  |_  \_ |__ ___.__. _____ _/  |____  ___
 |       _/\__  \ |  |/ __ |     |    |  _//  _ \   __\  | __ <   |  | \__  \\   __\  \/  /
 |    |   \ / __ \|  / /_/ |     |    |   (  <_> )  |    | \_\ \___  |  / __ \|  |  >    < 
 |____|_  /(____  /__\____ |_____|______  /\____/|__|    |___  / ____| (____  /__| /__/\_ \


'''
# Impression de l'ASCII art avec des couleurs
print(colored(ascii_art, 'cyan'))

# Menu avec les options colorées
print(colored("[1.] Preset Nuke", 'red'))
print(colored("[2.] Nuke personalisé", 'green'))

# Option choisie
print(colored("[ ? ] Option choisi : ", 'white'), end='')

# Lecture de l'option choisie par l'utilisateur
option = input()

if option == '1':
    # Aller dans le dossier main_code et exécuter nukepreset.py
    try:
        os.chdir('main_code')
        subprocess.run(['python', 'nukepreset.py'])
    except Exception as e:
        print(colored(f"Erreur lors de l'exécution de nukepreset.py : {e}", 'red'))
elif option == '2':
    # Aller dans le dossier main_code et exécuter nukeperso.py
    try:
        os.chdir('main_code')
        subprocess.run(['python', 'nukeperso.py'])
    except Exception as e:
        print(colored(f"Erreur lors de l'exécution de nukeperso.py : {e}", 'red'))
else:
    print(colored("Option non valide ou non implémentée.", 'yellow'))

# Désinitialisation de colorama
colorama.deinit()