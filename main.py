import os
import subprocess
import colorama
from termcolor import colored

# Initialisation de colorama
colorama.init()

# ASCII Art
ascii_art = '''
__________        .__    .___   _________            .__        __    ________  .__                              .___
\______   \_____  |__| __| _/  /   _____/ ___________|__|______/  |_  \______ \ |__| ______ ____  ___________  __| _/
 |       _/\__  \ |  |/ __ |   \_____  \_/ ___\_  __ \  \____ \   __\  |    |  \|  |/  ___// ___\/  _ \_  __ \/ __ | 
 |    |   \ / __ \|  / /_/ |   /        \  \___|  | \/  |  |_> >  |    |    `   \  |\___ \\  \__(  <_> )  | \/ /_/ | 
 |____|_  /(____  /__\____ |  /_______  /\___  >__|  |__|   __/|__|   /_______  /__/____  >\___  >____/|__|  \____ | 


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
