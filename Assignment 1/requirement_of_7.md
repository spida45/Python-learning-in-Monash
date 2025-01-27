# Task 7 - Adding a little ✨ Magic ✨ (28%)

Good job! You now have a functioning game of Snakes and Ladders! 

We are now going to make our game epic by adding a few surprises and making a couple of improvements.

So copy all your functions from task 6 over, and then make the following improvements and additions:

## Improvements
- We are going to replace the individual lists that were being returned from the initialise game and swap them for a dictionary called `game` that has the following keys:

  * `players` : A dictionary that has the names of the players playing the game as its keys and the positions as its values.

  * `snakes` : A dictionary that has the snake heads as its keys and the tails as its values.

  * `ladders` : A dictionary that has the ladder bases as its keys and the tops as its values.

- The `play_game` function should now return the name of the winning player. 

> You should take care to NOT call get_num_players in play_game.

- We are also going to improve the `pick_winner` function which will now take the players dictionary and return the name of the winning player. If no player is the winner, it should return None.

- Introduce a new function called `turn_by_turn_gamep`lay that plays a manual 2-person game with each player manually completing each turn by action. In this function, re-use the functions that you have created before and make it so that each player has to enter roll as an input to `roll` the dice or quit to `quit` the game at any stage. There are no automated tests for this function so you should check its functionality manually. You can and should use the functions that you have already defined.

## Surprises! 
We are going to introduce 'power tiles' to the game! 

At the beginning of the `play_game` function, call the function `generate_surprises` which returns a list of surprise tile locations. These should then be added to the dictionary `game` under the key `surprise_tiles`.

When a player lands on one of these tiles, a special dice with 3 sides is rolled by calling the function `special_roll()` and it returns a value from 0,1 or 2. The value determines what should happen as explained below: 

- If the special roll is a 0, then the current player gets to roll once again (**this means still the same player rolls normal dice again**).

- If the special roll is a 1, then the player after the current player loses a turn.

- If the special roll is a 2, then all other players on the board move back 5 spaces. If moving back a player puts their position below 0, then place them back on 0 (**No further updates due to step on the ladder base or snake head need to be considered**).

The functions `generate_surprises` and `special_roll` have already been defined and imported into the game for you. Feel free to copy and paste the functions that you created from the previous task here. A scaffold has been provided for you.

> You need to ensure that the `turn_by_turn_gameplay` function includes this new roll as well. Therefore, you should re-use some of these functions and create more functions if you need! 

> Another point to note is that the snakes and ladders take priority over special roll. If the final position after climbing up a ladder/going down a snake is a special tile then you should special roll.
For example, if there is a ladder base at position 25 and it also happens to be a special tile, then you should move up the ladder instead of applying the special roll. 
Another scenario would be where the player lands on a ladder base at position 25 and climbs up to position 67, which happens to be a surprise tile. In this case, once the player has climbed up the ladder, they should then roll the special dice.