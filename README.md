# Sports Quiz

The sports quiz application is a quiz game which will display questions for the user to answer. All sports based so it is targeted and probably would appeal more to sports fans but can be enjoyed by anyone. This project gave me the chance to work with an API and this is how the users scores and username are kept and this is updated on an excel spreadsheet once they have completed the quiz. I created the sports quiz as a way to make a fun and entertaining game that anyone can enjoy. The game will become more and more entertaining as questions will be added in the future. This will keep the game entertaining and users coming back to play.&nbsp;

![amiresponsive](https://user-images.githubusercontent.com/91072896/154056148-34a77624-4b4b-48cc-85b5-2e1100de39d2.png)

# Table of Contents
1. [UI](#id-ui)
2. [Features](#id-features)
3. [Testing](#id-testing) 
4. [Validator Testing](#id-validator)
5. [Bugs](#id-bugs)
6. [Unfixed Bugs](#id-bugs)
7. [Deployment](#id-deploy)
8. [Credits](#id-credits)
9. [Acknowledgements](#id-acknowledgements)

# UI<div id='#id-ui'/>
## User Stories

 ### As a User

  * As a user, I want a website that is easy to navigate.

  * As a user, I want clear instructions on how to play the game.

  * As a user, I want to see a game that will be playable on all devices and performace and experience will not change.

  * As a user, I want there to be a score counter, that will keep track of the scores.

  * As a user, I want there to be a leaderboard, that will display high scores.

  * As a user, I want there to be updated on the result once the game has finished.
 

### As a returning user

 * As a returning user, I want the website to be continually updated with new features and questions to keep me playing the game.


# Features<div id='#id-features'/>

### Home screen

The home screen is the first thing a user sees when they open the program. The title of the game is displayed on the home screen. There is an input field below it. Users are asked to enter their name here. In the future, this computer will be able to refer back to the user by name. The user is then prompted to press enter to return to the main menu.
&nbsp;

![homescreen](https://user-images.githubusercontent.com/91072896/154067753-306850b1-e98b-4e97-b566-b1cbf0175117.png)

### Main menu

The user will be directed here once they press enter. The main menu has four options for the user. To access these sections, the user simply presses either a, b, c or d. The user can start the game, read instructions view the leaderboard and exit the game. As this input is validated, the user will not be able to continue unless one of the valid options is selected.&nbsp;

![menu](https://user-images.githubusercontent.com/91072896/154072579-d524c1de-9941-451a-bb82-a4f8aa847a1a.png)

### The game

The game begins once the user initiates the start game function. The game will begin with one question. The user will be shown a question with four possible answers. The user will then be asked to select one. After answering the question, they will be prompted with a correct or incorrect answer, and the next question will be displayed. If they enter an incorrect input, the game will not continue until a valid input is entered. A screenshot illustrates this.&nbsp;

![invalid-input](https://user-images.githubusercontent.com/91072896/154068087-c00ca410-e1ce-4a1f-8555-34ed46d7e50f.png)

### The scores

The game will run through all the questions and once all twelve have been answered the quiz is completed. Upon completion of the game, the user will receive the score they achieved out of the twelve questions. Then there is also an option for the user to play the game again. The user will be able to repeat the same process and run through all the questions again. Additionally, the user has the option to refuse to play, which will end the game. They will be prompted by a message and will have to click the 'run program' button to restart the application.&nbsp;

![final-score](https://user-images.githubusercontent.com/91072896/154068223-3397c837-5448-412a-8d9e-654654f01f5e.png)

### The Leaderboard

The leaderboard collects the top five scores of the game and displays them in order of the highest. The scores when submitted an API google spreadsheet. That information is then taken from the spreadsheet and displayed in the leaderboard it will take the highest scores no matter what order they are in the spreadsheet. THis is a great feature as this allows the users to check their progress and see what they have to do to climb up that leaderboard.&nbsp;

![leaderboard](https://user-images.githubusercontent.com/91072896/154074463-5a68b7a2-3b29-4936-bcea-3b2e52a5b0a4.png)

### Google spreadsheets

This is where the user name and final scores are stored. Once the user finishes the quiz it calculates that users score to the spreadsheet. The leaderboard then pulls the top five with the highest scores and then displays them in order on the leaderboard. page.&nbsp;
![google-spreadsheet](https://user-images.githubusercontent.com/91072896/154124060-38d756ae-50bb-4adb-b024-cc55bd790c83.png)


### The instructions

At the main menu, the second option that customers can choose to select is instructions. Selecting this option will bring them to the instructions page. Here the customer is shown the instructions of how to play the game. There is also a prompt at the bottom of the page instructing users to press the letter 'r' to return to the main menu.&nbsp;

![instructions](https://user-images.githubusercontent.com/91072896/154068293-685b5759-363b-45f1-a568-4da3f96184d0.png)

### Exit

The final option on the main menu is for the users to exit the game. The customer types the letter c the game ends wwith a message to 'run program' to restart the application.&nbsp;

![exit](https://user-images.githubusercontent.com/91072896/154075591-14f4658b-f342-4ce3-8e2b-095be313fc7c.png)

### Features Left to Implement

* I would definetly add more questions in the future as there are only twelve questions there at the moment this would add a better experience for the user if ther are many more questions that they can play through.

* A feature that I would also implemet would be to apply a time stamp to the leaderboard and google spreadsheet as it this will give the user more information aboutt their top scores if they play the gaem regularly and find themselves in the top five multiple times.

## Testing<div id='#id-testing'/>

* Accessibility
  * For the website, I used devtools to run lighthouse, and application scored well primarily on accessibility. Below are the results.&nbsp;

  ![lighthouse 1](https://user-images.githubusercontent.com/91072896/154124927-d18e2334-4205-469e-ac93-f4fd89f126e2.png)
