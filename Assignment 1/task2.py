'''
Task 2 - Implementing Basic Movement (8%)
Now that the game environment is set up, it is time to implement basic movement for the players on the game board. You will use variables and expressions to calculate the new positions of the players based on their dice rolls.

We are going to use a pre-defined function to generate a dice roll. You will learn more about functions in Week 3. However, for this task, just assume that dice roll will contain an integer between 1 and 6 (included) just like when you roll a six sided dice.

You are required to complete the following task:

Copy and paste all the code from Task 1 (except the print statements at the end).

Change the players' positions based on dice rolls. We are going to simulate one dice roll for each of the players.

Set the new position of the player as the position after the dice roll. Make sure to use the same variable names as in the previous tasks or the tests will fail.

Make sure you check that the player should not go over a 100 in their position. Even though we are only simulating one dice roll and it is impossible to go over a 100 with one roll, we need this logic for future tasks. If the total is going to cross 100, then ignore the dice roll and don't change the position.

For example:
Player Red is on 96.

Player Red rolls a 5, and hence, their dice roll is ignored. Player Red stays on 96.
'''

# DO NOT delete this line
from diceroll import roll_the_dice
import random

# Copy and paste the work from Task 1 here
# Player 1 Name
p1_name = input("Please input Player1 name:")

# Player 1 Position
p1_position = 0

# Player 2 Name
p2_name = input("Please input Player1 name:")

# Player 2 Position
p2_position = 0

# Snake Head Positions
def generate_snake_list(length):
    heads = [random.randint(1, 100) for _ in range(length)]
    tails = [random.randint(1, heads[i]) for i in range(length)]
    return heads, tails

length_snake = 5
snake_heads, snake_tails = generate_snake_list(length_snake)

# Snake Tail Positions
#snake_tails =
print("snake_heads", snake_heads)
print("snake_tails", snake_tails)


# Ladder Base Positions
def generate_ladder_list(length):
    bases = [random.randint(1, 100) for _ in range(length)]
    tops = [random.randint(bases[i], 100) for i in range(length)]
    return bases, tops

length_ladder = 5
ladder_bases, ladder_tops = generate_ladder_list(length_ladder)

# Ladder Tops Positions
#ladder_tops =
print("ladder_bases", ladder_bases)
print("ladder_tops", ladder_tops)


# Task 2 begins here

# Roll the dice for the first player
diceroll = roll_the_dice()

# Write the logic to move the first player
p1_position += diceroll

# Roll the dice for the second player
diceroll = roll_the_dice()

# Write the logic to move the second player
p2_position += diceroll

# Print the position of the first player
print("Player", p1_name, "is in position", p1_position)

# Print the position of the second player
print("Player", p2_name, "is in position", p2_position)
