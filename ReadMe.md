# Octi’s Battleship.

Octi’s Battlship is a simple terminal Python game, which runs on the heroku terminal.

  

Users can try and sink a battleship of random size randomly placed board of the size of the user's choosing.

  

Here is a link to my [<ins>project</ins>](https://octisbattleship.herokuapp.com/).

  ![Battleship.PNG](images\Battleship.PNG)
  



## How to play.

Octi’s Battleship is based on the famous pen and paper game of the same name. 

This version simplified with only one ship and the user is the only one attacking. The user enters the size they want to board to be then a ship is randomly generated and placed on the board. 

Cells are represented by O and a miss by an *, when the ship is hit it is represented as an X.

The player wins when he has sunk the battleship. 

  

## Features

### Existing Features 

The user can set the size of the board.

The user cannot see where the ship is.
![ddddd.PNG](images\ddddd.PNG)



The ship size and location is randomly generated.

You play against the computer.

The program accepts user input.

  

Input validation and error-checking is implemented. If the user inputs a coordonate that is off the grid it will let the user know and restart the round. If the user inputs letters at any time the program will ask the user for numbers again. Finally if the user inputs the same guess twice it will let the user know and ask for new coordinates again.
![badinput.PNG](images\badinput.PNG)



### Future Features.

Have to board so as to have the computer shoot back!

Allow players to position their ship.

Have multiple ships.

Keep score.

Have a restart button.

  

### Data Model.

The program is based on lists, variables and functions to manipulate and iterate through them. 

A list contains the play board and another the ship’s coordinates. 

  

The user's guesses are then compared to the ship's coordinates in the list and removed if they match. The list of the board is then appended with the appropriate symbol for a miss or a hit. 

Then a simple while loop checks if there are any more coordinates within the ship variable and continues if there are and ends the game if the number of coordinates is equal to 0. 

  

Functions are also used to help the user keep track of the game by updating the board, giving feedback on the shots and ending or continuing the game. 

  

While loops are used to check for the appropriate inputs as to not crash the programs when an out of bounds coordonate is given or something other than a number imputed.

  

### Testing

I have manually tested the project doing the following:

 Passing the code through a PEP8 linter, it has returned on line 4 and 19 continuation line missing indentation or outdented, this is however just for the ascii art. 

I and friends have passed it strings when numbers were expected multiple times, the code did not throw an error. Same with out of bounds input.

  

Tested on PowerShell terminal and Heroku terminal.

### Bugs 

#### Solved bugs 

Inputting letters would trough a Value Error as letters cannot be converted into integers, it was solved by using a try except method.

The try except method would pass the functions in the user guess function a value of None before looping out the try, which would trough an Index error as a none value cannot be iterated in the build board function. This was solved by warping the try except block in a while loop. 

#### Remaining bugs 

No remaining bugs 

#### Validator testing 

PEP8 came up with on line 4 and 19 continuation line missing indentation or outdented, this is however just for the ascii art.

  

### Deployment 

Steps for deployment 

 Created a new Heroku app 

 Set Buildbacks to python and NodeJS in that order 

 Linked the Heroku app to the repository 

 And then deployed. 

### Credits 

Code institute for deployment terminal.

[<ins>https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605</ins>](https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605) for solving the issue of a try except block returning none to a function.

[<ins>https://bigmonty12.github.io/battleship</ins>](https://bigmonty12.github.io/battleship) for the ship that are more than the size of 1.**