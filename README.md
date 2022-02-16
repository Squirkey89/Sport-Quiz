# Sports Quiz

The sports quiz application is a quiz game which will display questions for the user to answer. All the questions are sports based so it is targeted towards sports fans. However it is a fun challenging game so the aim is to keep users coming back. This project gave me the chance to work with an API and this is how the users scores and username are kept and this is updated on an excel spreadsheet once they have completed the quiz. I created the sports quiz as a way to make a fun and entertaining game that anyone can enjoy. The game will be updated with new questions added in the future. This will keep the game entertaining and users coming back to play.&nbsp;

![amiresponsive](https://user-images.githubusercontent.com/91072896/154056148-34a77624-4b4b-48cc-85b5-2e1100de39d2.png)

# Table of Contents
1. [Flow Chart](#id-flow)
2. [UI](#id-ui)
3. [Features](#id-features)
      * [Home Screen](#id-home)
      * [Main Menu](#id-menu)
      * [The Game](#id-game)
      * [The Scores](#id-scores)
      * [The Leaderboard](#id-leaderboard)
      * [Google Spreadsheet](#id-spreadsheet)
      * [The Instructions](#id-instructions)
      * [Exit](#id-exit)
      * [Features left to implement](#id-implement)
4. [Invalid input](#id-invalid)
5. [Testing](#id-testing) 
6. [Bugs](#id-bugs)
7. [Unfixed Bugs](#id-unfixed)
8. [Technologies Used](#id-tech)
9. [Deployment](#id-deploy)
10. [Credits](#id-credits)
11. [Acknowledgements](#id-acknowledgements)

# Flow Chart<div id='id-flow'>
This flow chart I created shows the structure of the application I entended to create.&nbsp;

![flowchart](https://user-images.githubusercontent.com/91072896/154189015-870768d2-fe3c-4f6e-ad98-064ee7858ef7.png)



# UI<div id='id-ui'>
# User Stories

 ## As a User

  * As a user, I want a website that is easy to navigate.

  * As a user, I want clear instructions on how to play the game.

  * As a user, I want there to be a score counter, that will keep track of the scores.

  * As a user, I want there to be a leaderboard, that will display high scores.

  * As a user, I want there to be updated on the result once the game has finished.
 

## As a returning user

 * As a returning user, I want the website to be continually updated with new features and questions to keep me playing the game.

  * As a returning user, I want to be able to challenge my friends.



# Features<div id='id-features'>

## Home screen <div id='id-home'>

The home screen is the first thing a user sees when they open the program. The title of the game is displayed on the home screen. There is an input field below it. Users are asked to enter their name here. Once the name is entered the computer will be able to refer back to the user by name. The user is then prompted to press enter to return to the main menu.
&nbsp;

![homescreen](https://user-images.githubusercontent.com/91072896/154067753-306850b1-e98b-4e97-b566-b1cbf0175117.png)

## Main menu <div id='id-menu'>

The user will be directed here once they press enter. The main menu has four options for the user. To access these sections, the user simply presses either a, b, c or d. The user can start the game, read instructions view the leaderboard and exit the game. As this input is validated, the user will not be able to continue unless one of the valid options is selected.&nbsp;

![menu](https://user-images.githubusercontent.com/91072896/154072579-d524c1de-9941-451a-bb82-a4f8aa847a1a.png)

## The game <div id='id-game'>

The game begins once the user initiates the start game function. The game will begin with one question. The user will be shown a question with four possible answers. The user will then be asked to select one. After answering the question, they will be prompted with a correct or incorrect answer, and the next question will be displayed. If they enter an incorrect input, the game will not continue until a valid input is entered. A screenshot illustrates this.&nbsp;

![invalid-input](https://user-images.githubusercontent.com/91072896/154068087-c00ca410-e1ce-4a1f-8555-34ed46d7e50f.png)

## The scores <div id='id-scores'>

The game will run through all the questions and once all twelve have been answered the quiz is completed. Upon completion of the game, the user will receive the score they achieved out of the twelve questions. Then there is also an option for the user to play the game again. The user will be able to repeat the same process and run through all the questions again. Additionally, the user has the option to refuse to play, which will end the game. They will be prompted by a message and will have to click the 'run program' button to restart the application.&nbsp;

![final-score](https://user-images.githubusercontent.com/91072896/154068223-3397c837-5448-412a-8d9e-654654f01f5e.png)

## The Leaderboard <div id='id-leaderboard'>

The leaderboard collects the top five scores of the game and displays them in order of the highest. The scores when submitted an API google spreadsheet. That information is then taken from the spreadsheet and displayed in the leaderboard it will take the highest scores no matter what order they are in the spreadsheet. This is a great feature as this allows the users to check their progress and see what they have to do to climb up that leaderboard.&nbsp;

![leaderboard](https://user-images.githubusercontent.com/91072896/154074463-5a68b7a2-3b29-4936-bcea-3b2e52a5b0a4.png)

## Google spreadsheets <div id='id-spreadsheet'>

This is where the user name and final scores are stored. Once the user finishes the quiz it calculates that users score to the spreadsheet. The leaderboard then pulls the top five with the highest scores and then displays them in order on the leaderboard. page.&nbsp;

![google-spreadsheet](https://user-images.githubusercontent.com/91072896/154124060-38d756ae-50bb-4adb-b024-cc55bd790c83.png)


## The instructions <div id='id-instructions'>

At the main menu, the second option that customers can choose to select is instructions. Selecting this option will bring them to the instructions page. Here the customer is shown the instructions of how to play the game. There is also a prompt at the bottom of the page instructing users to press the letter 'r' to return to the main menu.&nbsp;

![instructions](https://user-images.githubusercontent.com/91072896/154068293-685b5759-363b-45f1-a568-4da3f96184d0.png)

## Exit <div id='id-exit'>

The final option on the main menu is for the users to exit the game. The customer types the letter 'd' the game ends wwith a message to 'run program' to restart the application.&nbsp;

![exit](https://user-images.githubusercontent.com/91072896/154075591-14f4658b-f342-4ce3-8e2b-095be313fc7c.png)

## Features Left to Implement <div id='id-implement'>

* I would add more questions to the application in the future. At present there are only twelve questions, consistently updating the questions would add a better experience for the user. The more questions available the more content for the user to take part in.

* A feature that I would also implement would be to apply a time stamp to the leaderboard and google spreadsheet as it this will give the user more information about their own top scores if they play the game regularly and find themselves in the top five multiple times. The time stamp will distinguish when they achieved those scores.

* Furthermore, I would like to add a feature in the future that allows players to play against each other. A user can choose from a number of questions, and then both players can go head to head over them.

# Invalid input

## Enter Name
  As the user starts the game they will have to enter their name to begin. If the user leaves any white spaces or just presses enter they will not be able to proceed. An error message will be displayed and the user cant continue until a valid input is entered.&nbsp;

![name-val](https://user-images.githubusercontent.com/91072896/154194873-309cf2c4-c1ed-4380-a6bc-39d6d7f5abe4.png)

## Menu
  The user will have four options in the main menu screen. If they decide to choose an invalid character an error message is displayed and they are prompted to enter a, b, c or d. I also used strip() and upper() on all the inputs fields if the user leaves a blank by accident and then enters a valid input then the option choosen will be accepted.&nbsp;

  ![menu-val](https://user-images.githubusercontent.com/91072896/154193240-6eb3d169-a33f-4e2f-8681-79350be91d21.png)

## Leaderboard/Instructions
  Leaderboard and instructions are grouped together because they both have the same input validation. Once you enter the leaderbord or instructions the onlyn way to return to main menu is to press the 'r' and failure to do this will result in invalid input and a prompt message to press 'r' to return.&nbsp; 

![instruct-val](https://user-images.githubusercontent.com/91072896/154193241-806bec41-c6b5-4383-9ee3-99d8f5a827d4.png)

![leaderboard-input-valid](https://user-images.githubusercontent.com/91072896/154193242-8f10b254-dc27-404f-a723-0c96999c4c27.png)

## Game
  The game is multiple choice so the user can in put a, b, c or d. An invalid input will result in the game pausing until the user enters valid input to the question asked. The game will not continue until on of these valid options are entered.&nbsp;

  ![game-val](https://user-images.githubusercontent.com/91072896/154193239-07e95fed-000e-4e2e-96c4-10323994d03e.png)

## Play Again
  When the game comes to an end after the twelve questions the user will be give an option to play again. The user can type 'y' to reply yes and the game will start again. If they type 'n' then the game will quit. Any other option choosen will result in an invalid input and the message shown below will be displayed.
  &nbsp;

  ![plagagain-val](https://user-images.githubusercontent.com/91072896/154193236-a5888a12-dff2-4da2-949b-53ecf247b4aa.png)


# Testing<div id='id-testing'>

## Lighthouse Validation
  * For the website, I used devtools to run lighthouse, and application scored well primarily on accessibility. Below are the results.&nbsp;

  ![lighthouse 1](https://user-images.githubusercontent.com/91072896/154124927-d18e2334-4205-469e-ac93-f4fd89f126e2.png)

## Pep8 Validation
  * I put the code through pep8 validation where it passed and this confirmed that there were no issues.&nbsp;

![pep8](https://user-images.githubusercontent.com/91072896/154150498-9fce554a-ed33-4859-a85f-837b1b2512b6.png)


## Heroku terminal
  * I began testing the code in the terminal in the gitpod workspace. Once I deployed the project and push my changes   
I could test it on the Heroku terminal.

## Search Engines
  * Google Chrome
  * Safari
  * Mozilla Firefox

## Devices
  * ASUS Chromebook Flip C434
  * Apple Macbook
  * Apple Ipad
  * Samsung Galaxy A50 
  * Iphone 12 

# Bugs<div id='id-bugs'>

As I was running my code through Pep8 validation, I found the lines to be too long. After some research I discovered I needed to use a backslash to separate the lines. Python requires backslashes to separate lines. I learned that Python accepts a limited number of characters on one line. I ran into another problem after adding this backslash. The backslash was followed by a long blank space when I entered the code in the terminal. With some help from my colleagues on Slack, I discovered that I could move the code to the next line to make more space. This ended up working perfectly. When I ran the code again, it passed Pep8 validation.&nbsp;

![error](https://user-images.githubusercontent.com/91072896/154170027-2d93c299-f0dc-4bf9-a24c-9f27a6e4a2e1.png)

# Unfixed Bugs<div id='id-unfixed'>
  
I encountered some problems while testing the application. The application worked well on most devices except for the Apple Ipad. So, the problem that arose was that when you opened the program and ran it, it brought you to the title screen where you had to enter a name. When you clicked on the area, a keypad appeared. However, once you entered the name and pressed the enter key, nothing appeared in the input field for name. I tried to fix this problem, but unfortunately after many attempts I was unable to do so. I tried getting help but was unsuccessful with that also, so that is why it is still unfixed.

# Technologies Used<div id='id-tech'>
  * Heroku
  * Github
  * Gitpod
  * Google Spreadsheets
  * Google Drive


# Deployment<div id='id-deploy'>
The website was deployed early on when I undertook the project. This was so I could test it early on. To deploy the website I used Heroku.

Following are the steps I took to deploy my Heroku project:

* The run.py file should be cleaned up of any unneeded imports.
* For input methods to work properly in the deployed mock terminal, add a new line character at the end of the text in the input '\n'.
* In the terminal, run the following command to create a list of requirements: pip3 freeze > requirements.txt
* In your Heroku account, click 'Create New App' in the Dashboard. Name the application and select Europe from the region dropdown menu.
* Press the "Create App" button.
* Config Vars should be set up in Settings (only if creds.json file is being used).
* To add the Python buildpack, click the ‘Add Buildpack’ button and then click the ‘Save Changes’ button.
* Next, choose ‘NodeJS’ and click save once more. Make sure your buildpacks are set up correctly. Python always goes on top of NodeJS. They can be moved around.
* Select the deployment tab.
* Choose 'GitHub' for your deployment method.
* Then search for the repository name. It will link to github and click connect
* Then click 'Enable Automatic Deployments'.
* In the Manual deploy section, select the main branch and click 'Deploy Branch'.
* Once the project is deployed, click ‘view’ to access deployed project.
* When returning to this page there is a view app button to get access to the application.

The live link to this website can be found here - https://sportsquiz1.herokuapp.com/

# Credits<div id='id-credits'>
## Content
  * I referenced a line of code from [Stackoverflow](https://stackoverflow.com/questions/30076145/how-to-sort-list-of-lists-by-highest-number). I used the code when I was trying to sort the list by the highest number. The code is: `sorted(l, key=lambda x: int(x[1]), reverse=True)`.
  * I also referenced the love maths project when transfering data from python to the spreadsheet in the update_worksheet function.
  * All the question that are used in the quiz were taken from [Open Trivia Database](https://opentdb.com/api_config.php)
  * [Am I Responsive](http://ami.responsivedesign.is/) was used for the header image that appears at the top of the read me file.
  * While researching the application that I would build I took inspiration from [Mike Dane](https://www.youtube.com/watch?v=SgQhwtIoQ7o&t=179s&ab_channel=MikeDane) and also from [Bro Code](https://www.youtube.com/watch?v=yriw5Zh406s&t=513s&ab_channel=BroCode). After viewing those videos this encouraged me to make a quiz game.

## Media
  * The large ascii text at the beginning of the game was used from a website called [patorjk](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) This website has loads of different styles available for text. The style I used is called 'Big moneyne'.
  * I used [lucid chart](https://lucid.app/lucidchart/9331c746-149f-43ee-99b4-f5d069569366/edit?beaconFlowId=7EBCDF6C52EB4D67&invitationId=inv_2f7a6c93-0720-4f95-821a-a505c29dcaa4&page=NfXTJ6v46zip#) to create my flow chart.

## Acknowledgments<div id='id-acknowledgements'>
  * My mentor for the useful feedback direction and guidance he has provided since the beginning of the course.
  * The online tutors help and and advice when stuck on a problem with no one else to turn too.
  * The slack community who are very helpful.
  * The Code Institite course material.