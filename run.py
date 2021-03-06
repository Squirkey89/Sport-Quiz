import gspread
from google.oauth2.service_account import Credentials
import random


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


def quiz_questions():
    """
    List of quiz questions and answers
    """
    questions = []
    questions.append([
        "Who won the 2018 Monaco Grand Prix?\n"
        "A: Lewis Hamilton\n" "B: Kimi Raikkonen\n"
        "C: Daniel Ricciardo\n" "D: Sebastien Vettel\n", "C"])
    questions.append([
        "Who won the Uefa Champions League in 1999?\n"
        "A: Barcelona\n" "B: Liverpool\n"
        "C: Manchester United\n""D: Bayern Munich\n", "C"])
    questions.append([
        "What national team won the 2016 UEFA European Championship?\n"
        "A: Portugal\n" "B: Germany\n"
        "C: England\n""D: France\n", "A"])
    questions.append([
        "Who was the topscorer for England national football team""?\n"
        "A: David Beckham\n" "B: Wayne Rooney\n"
        "C: Steven Gerrard\n""D: Michael Owen\n", "B"])
    questions.append([
        "Who was the top scorer of the 2014 FIFA World Cup?\n"
        "A: Neymar\n" "B: Lionel Messi\n"
        "C: Thomas Müller\n""D: James Rodríguez\n", "D"])
    questions.append([
        "Which basketball team has attended the most NBA grand finals?\n"
        "A: Golden State Warriors\n" "B: Los Angeles Lakers\n"
        "C: Philadelphia 76ers\n""D: Boston Celtics\n", "B"])
    questions.append([
        "Who won the 2011 Stanley Cup?\n"
        "A: New York Rangers\n" "B: Montreal Canadiens\n"
        "C: Boston Bruins\n""D: Toronto Maple Leafs\n", "C"])
    questions.append([
        "Which soccer team won the Copa America,2015 Championship?\n"
        "A: Brazil\n" "B: Argentina\n"
        "C: Chile\n" "D: Paraguay\n", "C"])
    questions.append([
        "F1 Virtual Safety Cars were introduced after which driver's death?\n"
        "A: Jules Bianchi\n" "B: Ayrton Senna\n"
        "C: Ronald Ratzenberger\n""D: Gilles Villeneuve\n", "A"])
    questions.append([
        "Which country is hosting the 2022 FIFA World Cup?\n"
        "A: Quatar\n" "B: Uganda\n"
        "C: Vietnam\n""D: Bolivia\n", "A"])
    questions.append([
        "Which golfer won the the 2019 Masters tournament?\n"
        "A: Bubba Watson\n" "B: Tiger Woods\n"
        "C: Rory McIllroy\n""D: Phil Mickelson\n", "B"])
    questions.append([
        "Which of the following Grand Slam tennis tournaments occurs last?\n"
        "A: Wimbledon\n" "B: Australian\n"
        "C: French Open\n""D: US Open\n", "D"])

    return questions


def start_screen():
    """
    This is the beginning of the quiz for
    the user they will first find an
    introduction to the game with the quiz
    name and images. Then they are
    prompted to press the enter key
    """

    print("""
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


start_screen()

NAME = input("Please enter your name\n")
while not NAME.strip():
    NAME = input("Invalid, Please enter your name\n")
else:
    print(f"Hey {NAME}, Welcome to the Sports Quiz.\n")


start = input("Press enter to go to the main menu\n")


def instructions():
    """
    The user will be introduced to the
    instructions on how to play the quiz.
    """
    print("")
    print("***********************Instructions************************\n")
    print("")
    print("You will be tested on your sports knowledge with 12 questions.\n")
    print("The questions are multiple choice,you will pick a, b, c, or d.\n")
    print("The answer to the question will be displayed once you choose.\n")
    print("When the question is answered, the next question will appear.\n")
    print("You will receive your result at the end. Best of luck!!!\n")
    print("")

    while True:
        return_menu = input("Press the letter 'r' to return to menu screen.\n")
        return_menu = return_menu.upper()
        return_menu = return_menu.strip()

        if return_menu == 'R':
            main_menu()
        else:
            print("Your choice is incorrect please choose a valid option\n")


def leaderboard():
    """
    This page displays the users scores
    """
    print("***********************Leaderboard************************\n")
    print()
    score_sheet = SHEET.worksheet("score").get_all_values()[1:]
    for data in score_sheet:
        data[1] = (data[1])

    update_data = sorted(score_sheet, key=lambda x: int(x[1]), reverse=True)

    print("---------------------Top 5 Scores-------------------------")
    print("")
    print("Pos \tName \tScore")

    if(len(update_data) < 5):
        count = len(update_data)
    else:
        count = 5

    for i in range(0, count):
        print(f"{i+1}\t{update_data[i][0]}\t{update_data[i][1]}")
        print("")

    while True:
        return_menu = input("Press the letter 'r' to return to menu screen.\n")
        return_menu = return_menu.upper()
        return_menu = return_menu.strip()

        if return_menu == 'R':
            main_menu()
        else:
            print("Your choice is not a valid option \n")


def play_quiz_game():
    """
    This is the Quiz for the user to play it is multiple choice
    and has four options for the user to choose from.
    I am able to take control, is there any chat option in this app?
    """

    questions = quiz_questions()
    random.shuffle(questions)
    points = 0

    for question in questions:
        print("***********************Sports Quiz************************\n")
        print()
        print(question[0])

        valid_options = ['A', 'B', 'C', 'D']
        user_input = input("Choose one of the options:\n")
        user_input = user_input.upper()
        user_input = user_input.strip()
        correct_answer = question[1]

        while(user_input not in valid_options):
            print('Invalid Input, please try again')
            user_input = input('Choose one of the options: a, b, c, d \n')
            user_input = user_input.strip()
            user_input = user_input.upper()
        if user_input not in valid_options:
            print("Invalid input")
        elif user_input == correct_answer:
            print("Correct! Well done.")
            points = points + 1
        elif user_input != correct_answer:
            print("Incorrect! Unlucky.")

    print("")
    point(points, NAME)
    update_worksheet(NAME, points, 'score')
    print("")
    play_again()


def point(points, NAME):
    """
    Score function keeps the score of the quiz game.
    Once the quiz is finished the result is printed.
    """
    num_questions = 12

    if points >= 8:
        print(f"Great job {NAME}. You scored {points} out of {num_questions}")
        print("")
    elif points < 8:
        print(f"Not bad {NAME}. You scored {points} out of {num_questions}")
        print("")


def play_again():
    """
    This is available to players once they finish the quiz.
    The user has the option to play again.
    """
    valid_options = ['Y', 'N']
    replay = input("Do you want to play again? y/n\n")
    replay = replay.upper()
    replay = replay.strip()

    while(replay not in valid_options):
        print('Invalid Input, please try again')
        replay = input("Please enter your choice here: y/n\n")
        replay = replay.upper()
        replay = replay.strip()
    if replay not in valid_options:
        print("Your choice is incorrect please choose a valid option\n")
        input("Choose one of a,b,c:")
    if replay == 'Y':
        play_quiz_game()
    elif replay == 'N':
        print("Click 'Run program' to restart")
        quit()


def main_menu():
    """
    Upon passing the start screen. The user will be presented
    with three options. First to play the game.
    The second option is Instructions for playing the game.
    The final option for the user is to exit the game.
    """

    print("***********************Main Menu************************\n")

    print(""" A: Start Game\n B: Instructions\n C: Leaderboard\n D: Exit\n """)
    valid_options = ['A', 'B', 'C', 'D']
    choice = input("Please enter your choice here:\n")
    choice = choice.upper()
    choice = choice.strip()
    print()

    while(choice not in valid_options):
        print('Invalid Input, please try again')
        choice = input("Please choose a,b,c,d:\n")
        choice = choice.upper()
        choice = choice.strip()
    if choice not in valid_options:
        print("Your choice is incorrect please choose a valid option\n")
        input("Choose one of a,b,c,d:")
    if choice == "A":
        play_quiz_game()
    elif choice == "B":
        instructions()
    elif choice == "C":
        leaderboard()
    elif choice == "D":
        print("Click 'Run program' to restart")
        quit()


def update_worksheet(username, points, worksheet_name):
    """
    This will update a new row in th sports_quiz worksheet
    This updates a new row with the username and score.
    """
    print(f"Updating {worksheet_name} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet_name)

    worksheet_to_update.append_row([username, points])

    print(f"{worksheet_name} Worksheet updated successfully\n")


def main():
    """
    The main function calls the functions to play the game.
    """
    main_menu()
    play_quiz_game()
    play_again()

main()
