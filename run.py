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

    name = input("Please enter your name\n")
    print(f"Hey {name}, Welcome to the Sports Quiz.\n")

start_screen()


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
        print("Your choice is incorrect please pick a valid choice\n")


def main_game():
    """
    This is the Quiz for the user to play it is multiple choice
    and has four options for the user to choose from.
    """
play = True
while play:
    result = 0
    questions = 11

    print("Let the quiz begin\n")

    question_answer = input("""1. Which country is hosting the 2022 FIFA World Cup?
    A: Quatar
    B: Uganda
    C: Vietnam
    D: Bolivia\n """)
    if question_answer.upper() == 'A':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'B' or 'C' or 'D':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d\n')

    question_answer = input("""2. Who won the 2018 Monaco Grand Prix?
    A: Lewis Hamilton
    B: Kimi Raikkonen
    C: Daniel Ricciardo
    D: Sebastian Vettel\n """)

    if question_answer.upper() == 'C':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'B' or 'A' or 'D':
        print('Unlucky incorrect answer\n')
    if not ('A', 'B' 'C' or 'D'):
        print('Invalid choice please choose A, B, C or D')

    question_answer = input("""3. Which basketball team has attended
    the most NBA grand finals?
    A: Golden State Warriors
    B: Los Angeles Lakers
    C: Philadelphia 76ers
    D: Boston Celtics\n """)
    if question_answer.upper() == 'B':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'B' or 'A' or 'D':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose A, B, C or D')

    question_answer = input("""4. Who won the Uefa Champions League in 1999?
    A: Barcelona
    B: Liverpool
    C: Manchester United
    D: Bayern Munich\n """)
    if question_answer.upper() == 'C':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'B' or 'A' or 'D':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose A, B, C or D')

    question_answer = input("""5. Which of the following Grand Slam tennis
    tournaments occurs LAST?
    A: Wimbledon
    B: Australian Open
    C: French Open
    D: US Open \n """)
    if question_answer.upper() == 'D':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'B' or 'A' or 'C':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose A, B, C or D')

    question_answer = input("""6. What national team won the 2016 edition
    of UEFA European Championship?
    A: Portugal
    B: Germany
    C: England
    D: France \n """)
    if question_answer.upper() == 'A':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'B' or 'D' or 'C':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose: A, B, C or D.')

    question_answer = input("""7. Who was the top scorer of the 2014 FIFA World Cup?",
    A: Neymar
    B: Lionel Messi
    C: Thomas Müller
    D: James Rodríguez\n """)
    if question_answer.upper() == 'D':
        print('Correct well done.!\n')
        result += 1
    elif question_answer.upper() == 'B'or 'A' or 'C':
        print('Unlucky incorrect answer.\n')
    else:
        print('Invalid choice please choose: A, B, C or D')

    question_answer = input("""8. Who won the 2011 Stanley Cup?",
    A: New York Rangers
    B: Montreal Canadiens
    C: Boston Bruins
    D: Toronto Maple Leafs \n """)
    if question_answer.upper() == 'C':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'B'or 'A' or 'D':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose: A, B, C or D')

    question_answer = input("""9. Who was the topscorer
    for England national football team?",
    A: David Beckham
    B: Wayne Rooney
    C: Steven Gerrard
    D: Michael Owen \n """)
    if question_answer.upper() == 'B':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'C'or 'A' or 'D':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose A, B, C or D')

    question_answer = input("""10. In Formula 1, the Virtual Safety Car was introduced
    following the fatal crash of which driver?",
    A: Jules Bianchi
    B: Ayrton Senna
    C: Ronald Ratzenberger
    D: Gilles Villeneuve \n """)
    if question_answer.upper() == 'A':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'C'or 'B' or 'D':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose A, B, C or D')

    question_answer = input("""11. Which soccer team won
    the Copa America 2015 Championship?",
    A: Brazil
    B: Argentina
    C: Chile
    D: Paraguay \n """)
    if question_answer.upper() == 'C':
        print('Correct well done!\n')
        result += 1
    elif question_answer.upper() == 'C'or 'A' or 'D':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose A, B, C or D')
    print(f"You correctly answered {result} out of {questions} questions\n")

    play_again = input("Do you want to again? y/n \n ")

    if play_again == 'Y' or play_again == 'y':
        playing = True
    elif play_again == 'N' or play_again == 'n':
        break
print('Thanks for playing :)\n')


main_menu()

main_game()
