# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """  _____ _   _  _____ _______       _____ _____            __  __   _____  ______ _____   ____  _____ _______ _____ _   _  _____   _______ ____   ____  _      
 |_   _| \ | |/ ____|__   __|/\   / ____|  __ \     /\   |  \/  | |  __ \|  ____|  __ \ / __ \|  __ \__   __|_   _| \ | |/ ____| |__   __/ __ \ / __ \| |     
   | | |  \| | (___    | |  /  \ | |  __| |__) |   /  \  | \  / | | |__) | |__  | |__) | |  | | |__) | | |    | | |  \| | |  __     | | | |  | | |  | | |     
   | | | . ` |\___ \   | | / /\ \| | |_ |  _  /   / /\ \ | |\/| | |  _  /|  __| |  ___/| |  | |  _  /  | |    | | | . ` | | |_ |    | | | |  | | |  | | |     
  _| |_| |\  |____) |  | |/ ____ \ |__| | | \ \  / ____ \| |  | | | | \ \| |____| |    | |__| | | \ \  | |   _| |_| |\  | |__| |    | | | |__| | |__| | |____ 
 |_____|_| \_|_____/   |_/_/___ \_\_____|_|  \_\/_/    \_\_|  |_| |_|  \_\______|_|     \____/|_|  \_\ |_|  |_____|_| \_|\_____|    |_|  \____/ \____/|______|
          (_) | | |     |  ____|  (_)   | |                                                                                                                   
 __      ___| |_| |__   | |__ _ __ _  __| | __ _ _   _                                                                                                        
 \ \ /\ / / | __| '_ \  |  __| '__| |/ _` |/ _` | | | |                                                                                                       
  \ V  V /| | |_| | | | | |  | |  | | (_| | (_| | |_| |                                                                                                       
   \_/\_/ |_|\__|_| |_| |_|  |_|  |_|\__,_|\__,_|\__, |                                                                                                       
                                                  __/ |                                                                                                       
                                                 |___/              """

urls = [
    "GitHub - https://github.com/fridayonline",
    "Instagram - https://instagram.com/fridayonline0",
    "Twitter - https://twitter.com/fridayonline0",
    "InstaReporter Tool - https://github.com/fridayonline/InstaReporter",
    ]

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Producer: Friday"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> Follow me On Instagram @fridayonline.")
    print ("\n", "-> Special For Hackers:\n    " + choice(urls))
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
