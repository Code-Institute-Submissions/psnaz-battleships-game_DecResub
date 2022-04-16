
![Battleships mockup](docs/images/battleships-mockup.png)

# BATTLESHIPS GAME
-----
Welcome to the Battleships, a fun online game for everyone who likes guessing!

Would you like to have fun and play a guessing game? Learn how to read coordinates and have fun guessing the location of small battleships. Can you locate all five battleships before you run out of shots? Let’s find out!


## Showcase
-----
A deployed link to the application can be found [here](https://battleship-game-by-ps.herokuapp.com/) and the Github repository link can be found [here.](https://github.com/psnaz/battleships-game)


## Features
-----
This simple online application is based on the traditional strategy board game Battleships played by two players. Battleships is a single player online application that teaches the user to state coordinates while playing a fun guessing game. The computer generates 5 single field battleships that are concealed on the board hidden from the player. On the screen the player can see a guessing board that records his guesses - hits or misses. 


### The Welcome Banner and Rules
The first thing the player sees when the application loads is a welcome banner and underneath are explained the Rules. The welcome banner and rules will display at the beginning of the game only.


### Guessing Board
Below the rules is displayed a guessing board (size 8 x 8) that records the guesses (hits and misses) the player takes. It shows two types of coordinates: Horizontal coordinates are letters from A to H. Vertical coordinates are numbers from 1 to 8. This board will get updated every time the player will take a guess. The hits are displayed as an X and the misses are displayed as a hyphen (-).

#### Asking for Coordinates (User’s Input)

The player is asked to enter a number between 1 and 8 first.

Then the player is asked to enter a letter between A and H.


If the player states a number or a letter outside the scope or accidentally presses enter key, he will be notified of his error and asked to provide the required input again.

#### Displaying Guesses and Shots Left

Player’s guesses are recorded on the guessing board while the player is always provided with relevant feedback for their action - whether they hit a ship or missed one.

They are also notified if they’ve accidentally guessed a coordinate they’ve used already.


After every  guess they’re also notified how many shots they have left.

#### The End of Game

How does the game end? 
The player wins the game if he shoots down all five ships before he runs out of shots.
won-screenshot

Or 

The player loses the game if he runs out of his 10 shots before he shoots down all five ships.


## User Experience (UX)
-----

### User Stories

The target audience (end users) of this project are players of all ages, predominantly children between 7-10 who like guessing games and would like to learn coordinates. 

The end user is looking for a fun way to be entertained while playing a guessing game and also learning to state coordinates.

The benefit of this project is fun and learning at the same time.

- As an end user I want to have some fun and learn to tell coordinates at the same time.
- As an end user I want to get excited about the chance 
- As an end user I want to receive clear instructions to be able to understand what this game is about, how to play it and be notified if I won or lost.
- As an end user I want to be able to read and understand the instructions easily.


## Strategy
-----
### Steps Taken

- Various Battleships game and tutorials researched on Google and Youtube

- Problems broken down, outlined and jotted down with pen and paper
- Tutorial to follow chosen
- GitHub repository created
- Building work/ Coding started by following the chosen tutorial
- Bugs fixed
- README file content outlined in Google docs
- No Mentor call scheduled due to time constraints and availability of the metro
- Project finalized and tested
- Project submitted to the Code Institute for marking


## Technologies Used
-----

### Languages Used

- Python

### Frameworks, Libraries and Programs Used

- Git: Git was used for version control by utilizing the Gitpod terminal - to commit to Git and push to GitHub
- GitHub: Github is used to store the project's code after being pushed from Git.
- Heroku: Heroku used to deploy the online application


## Credits
-----

### Code

#### The majority of the code came from:

- [’How to code Battleship in Python - Single Player Game’ tutorial](https://www.youtube.com/watch?v=tF1WRCrd_HQ) by Knowledge Mavens.
- CI Love Sandwiches Walkthrough project 

#### Otherwise based on the Diploma in Software Development study materials and my notes taken while going through the materials.

#### Other materials studied:

## Content
-----
-All content was written by the developer.

### Media

### Acknowledgements

## Testing
-----

## Unfixed Bugs
-----

## Deployment
-----

This site was deployed to Heroku pages by taking the following steps:
1. Log into your Heroku account
2. On your right hand side, click on the button ‘New’ and then click ‘create a new app’
3. Name your app and chose a region, then click ‘Create app’ button below
4. Click on the Settings in the tab
5. Click add Buildpack to add 2 buildpack as follows: first `heroku/python` and then `heroku/nodejs`, save changes
6. You must then create a Config var (click reveal Config Vars under the Settings, just above the Buildpack) called `PORT` (under key) and set it to `8000` (under value) and click add, then hide Config Vars
7. Click Deploy on the tab and chose deployment method: connect to your GitHub repository
8. Search for your repository, once found, connect.
9. Scroll down to Manual deploy and click ‘Deploy branch’. Your app will be built.
10. Once you ‘App was successfully deployed’ message and button with your deployed link, you can click on it to see your app.


### Forking the GitHub Repository

If you are interested how to fork this repository or how to make a local clone, this information can be found in Github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)


## Notes
-----
Unfortunately, I was not able to use my mentor’s help for this project as it took me much longer to go through the study materials. By then I felt it was pointless to start scheduling mentoring sessions. Also, I changed my mentor after the project 2 submission, so I only managed to schedule an introductory session. Also, later on my mentor’s availability around 2 weeks before Easter was very limited and I therefore decided to proceed with my project without my mentor’s help which obviously was not ideal.
I read the Project 3 Portfolio Guide and once I completed the Love Sandwiches walkthrough project decided to learn how to make the Battleship game rather than project focused on processing data. I mistakenly thought that the aim was to learn how to make the Battleship game and that’s why I watched quite a few tutorials and then decided to follow one () that I thought was well structured  despite having a bug because I was confident that I could fix it and possibly add to the game if I have a reasonable amount of time left.
I was able to fix the bug (if user pressed enter which was a string with an empty space’ the app crashed) with some help of tutoring.
Unfortunately, I came across  the Portfolio Project scope( Project Portfolio  Portfolio 3  Portfolio Project Scope)just two days before the project deadline which was too late so I am very concerned that my project doesn’t contain enough code produced just by myself.

