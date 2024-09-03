import os
from time import sleep

def cls():

    if os.name == 'nt':

        os.system('cls')

    else:

        os.system('clear')

cls()

if os.name == 'nt':

    print("Error - This script isn't supported on Windows, sorry :(")
    exit()

else:

    cls()

print('This script will now update packages and resolve dependencies')
sleep(3)
cls()
os.system('sudo apt upgrade -y')
os.system('sudo apt install -y gh git python3-colorama neofetch btop g++')
cls()
print('Done!')
