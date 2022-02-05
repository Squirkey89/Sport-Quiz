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

def main_game():
    """
    This is the Quiz for the user to play it is multiple choice
    and has four options for the user to choose from.
    """
    print("Let the quiz begin\n")

    question_answer = input("""Which country is hosting the 2022 FIFA World Cup?
    A: Quatar 
    B: Uganda
    C: Vietnam
    D: Bolivia\n """)
    if question_answer == 'A' or question_answer == 'a':
        print('Correct well done!\n')
    elif question_answer == 'B'or 'C' or 'D'or question_answer == 'b' or 'c' or 'd':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')

    question_answer = input("""Who won the 2018 Monaco Grand Prix?
    A: Lewis Hamilton 
    B: Kimi Raikkonen
    C: Daniel Ricciardo
    D: Sebastian Vettel\n """)
    if question_answer == 'C' or question_answer == 'c':
        print('Correct well done!\n')
    elif question_answer == 'B'or 'A' or 'D'or question_answer == 'b' or 'a' or 'd':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')
    
    question_answer = input("""Which basketball team has attended
    the most NBA grand finals?
    A: Golden State Warriors  
    B: Los Angeles Lakers
    C: Philadelphia 76ers
    D: Boston Celtics\n """)
    if question_answer == 'B' or question_answer == 'b':
        print('Correct well done!\n')
    elif question_answer == 'B'or 'A' or 'D'or question_answer == 'b' or 'a' or 'd':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')

    question_answer = input("""Who won the Uefa Champions League in 1999?
    A: Barcelona  
    B: Liverpool
    C: Manchester United
    D: Bayern Munich\n """)
    if question_answer == 'C' or question_answer == 'c':
        print('Correct well done!\n')
    elif question_answer == 'B'or 'A' or 'D'or question_answer == 'b' or 'a' or 'd':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')

    question_answer = input("""Which of the following Grand Slam tennis
    tournaments occurs LAST?
    A: Wimbledon  
    B: Australian Open
    C: French Open
    D: US Open \n """)
    if question_answer == 'D' or question_answer == 'd':
        print('Correct well done!\n')
    elif question_answer == 'B'or 'A' or 'C'or question_answer == 'b' or 'a' or 'c':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')

    question_answer = input("""What national team won the 2016 edition
    of UEFA European Championship?
    A: Portugal  
    B: Germany 
    C: England 
    D: France \n """)
    if question_answer == 'A' or question_answer == 'a':
        print('Correct well done!\n')
    elif question_answer == 'B'or 'D' or 'C'or question_answer == 'b' or 'd' or 'c':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')

    question_answer = input("""Who was the top scorer of the 2014 FIFA World Cup?",
    A: Neymar  
    B: Lionel Messi
    C: Thomas Müller
    D: James Rodríguez\n """)
    if question_answer == 'D' or question_answer == 'd':
        print('Correct well done!\n')
    elif question_answer == 'B'or 'A' or 'C'or question_answer == 'b' or 'a' or 'c':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')

    question_answer = input("""Who won the 2011 Stanley Cup?",
    A: New York Rangers  
    B: Montreal Canadiens
    C: Boston Bruins
    D: Toronto Maple Leafs \n """)
    if question_answer == 'C' or question_answer == 'c':
        print('Correct well done!\n')
    elif question_answer == 'B'or 'A' or 'D'or question_answer == 'b' or 'a' or 'd':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')

    question_answer = input("""Who was the topscorer
    for England national football team?",
    A: David Beckham  
    B: Wayne Rooney
    C: Steven Gerrard
    D: Michael Owen \n """)
    if question_answer == 'B' or question_answer == 'b':
        print('Correct well done!\n')
    elif question_answer == 'C'or 'A' or 'D'or question_answer == 'c' or 'a' or 'd':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')

    question_answer = input("""In Formula 1, the Virtual Safety Car was introduced
    following the fatal crash of which driver?",
    A: Jules Bianchi  
    B: Ayrton Senna
    C: Ronald Ratzenberger
    D: Gilles Villeneuve \n """)
    if question_answer == 'A' or question_answer == 'a':
        print('Correct well done!\n')
    elif question_answer == 'C'or 'B' or 'D'or question_answer == 'c' or 'b' or 'd':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')

    question_answer = input("""Which soccer team won
    the Copa America 2015 Championship?",
    A: Brazil  
    B: Argentina
    C: Chile
    D: Paraguay \n """)
    if question_answer == 'B' or question_answer == 'b':
        print('Correct well done!\n')
    elif question_answer == 'C'or 'A' or 'D'or question_answer == 'c' or 'a' or 'd':
        print('Unlucky incorrect answer\n')
    else:
        print('Invalid choice please choose a, b, c or d')




def main_menu():
    """
    Upon passing the start screen. The user will be presented
    with three options. First to play the game.
    The second option is Instructions for playing the game.
    The final option for the user is to exit the game.
    """
    print("Main Menu\n")

    print(""" A: Start Game\n B: Instructions\n C: Exit\n """)
    choice = input ("Please enter your choice here:\n ")

    if choice == "a" or choice == "A":
        main_game()
    elif choice == "b" or choice == "B":
        instructions()
    elif choice == "c" or choice == "C":
        exit()
    else:
        print("Your choice is incorrect please pick a valid choice")



main_menu()
    
main_game()

