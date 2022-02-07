import gspread
from google.oauth2.service_account import Credentials
from questions import questions

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

    username = input("Please enter your name\n")
    print(f"Hey {username}, Welcome to the Sports Quiz.\n")


start_screen()
start = input("Press enter to got to the main menu\n")

def main_menu():
    """
    Upon passing the start screen. The user will be presented
    with three options. First to play the game.
    The second option is Instructions for playing the game.
    The final option for the user is to exit the game.
    """
    
    print("Main Menu\n")

    print(""" A: Start Game\n B: Instructions\n C: Exit\n """)
    choice = input("Please enter your choice here:\n")

    if choice == "a" or choice == "A":
        main_game()
    elif choice == "b" or choice == "B":
        instructions()
    elif choice == "c" or choice == "C":
        exit()
    else:
        print("Your choice is incorrect please choose a valid option\n")
        input("Choose one of a,b,c:")


def main_game(questions):
    """
    This is the Quiz for the user to play it is multiple choice
    and has four options for the user to choose from.
    """

main_menu()


play = True
while play:
    result = 0
    questions = 11

    print("Let the quiz begin\n")


main_game()
