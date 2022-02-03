import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('sports_quiz')

score = SHEET.worksheet('score')

data = score.get_all_values()


def start_screen():
    """
    This is the beginning of the quiz for the user
    they will  first find an introduction to the game
    with the quiz name and images.
    Then they are prompted to press the enter key
    """


    print(f"""
  /$$$$$$                                  /$$
 /$$__  $$                                | $$
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$$
|  $$$$$$  /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/  /$$_____/ 
 \____  $$| $$  \ $$| $$  \ $$| $$  \__/  | $$   |  $$$$$$    
 /$$  \ $$| $$  | $$| $$  | $$| $$        | $$ /$$\____  $$
|  $$$$$$/| $$$$$$$/|  $$$$$$/| $$        |  $$$$//$$$$$$$/   
 \______/ | $$____/  \______/ |__/         \___/ |_______/  
          | $$                                                       
          | $$                                                                                     
          |__/ 
  /$$$$$$            /$$          
 /$$__  $$          |__/             
| $$  \ $$ /$$   /$$ /$$ /$$$$$$$$          
| $$  | $$| $$  | $$| $$|____ /$$/           
| $$  | $$| $$  | $$| $$   /$$$$/            
| $$/$$ $$| $$  | $$| $$  /$$__/           
|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$$ 
\____ $$$ \______/ |__/|________/    
""")

    key = input("Press the enter key to go to the main menu\n")

start_screen()

def main_menu():
    """
    Upon passing the start screen. The user will be presented 
    with three options. First to play the game.
    The second option is Instructions for playing the game.
    The final option for the user is to exit the game.   
    """
    print("Main Menu\n")

    choice = input(""" A: Start Game\n B: Instructions\n C: Exit\n
    Please enter your choice here:\n """)

    if choice == "a" or choice == "A":
        main_game()
    elif choice == "b" or choice == "B":
        instructions()
    elif choice == "c" or choice == "C":
        exit()
    else:
        print("Your choice is incorrect please pick a valide choice")


    
main_menu()

def exit():
    """
    This is when the user can exit the main menu
    The user will return to the start screen
    """
    start_screen()

exit()
 