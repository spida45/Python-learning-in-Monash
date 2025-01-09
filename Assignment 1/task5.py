'''
Task 5 - The More The Merrier! (12%)
Okay! So hopefully now you have got a fun little text-based game of Snakes and Ladders to play with your teammate.

What we are going to do in this task is extend your game you have built so far, and make it include multiple players!

You must use the variables players and positions to store the multiple players.

At the start of the game, you should ask the user for input on how many players they would like to play (minimum 1 and up to and including 4) and then you will need to modify your game such that all 4 players can play.

The order to follow for turns is:

Red -> Blue -> Green -> White

This is also the order in which the players get added to the game.

For example, if 3 players are going to play the game, then Red, Blue, and Green are added in that order.

You must use the same snakes and ladder positions from the previous task.

Also, feel free to print statements according to the previous task as well.

Similar to Task 4, once one player reaches 100, the game is over and you need to save the winning player's name in a variable called winner. You should then also print out a message declaring the winner.
'''

# DO NOT delete this line
from diceroll import roll_the_dice

# TODO: Task 5
players = ["Red", "Blue", "Green", "White"]
positions = [0, 0, 0, 0]
snake_heads = [25, 44, 65, 76, 99]
snake_tails = [6, 23, 34, 28, 56]
ladder_bases = [8, 26, 38, 47, 66]
ladder_tops = [43, 39, 55, 81, 92]
winner = ["Red", "Blue", "Green", "White"]
n = int(input("enter players' number\n"))
for i in range(n):
    players2 = players[: n]
    positions2 = positions[: n]
while all(x < 100 for x in positions2):
    flag = 0
    while flag < n:
        # Roll the dice for players
        diceroll = roll_the_dice()
        positions2[flag] += diceroll

        # Check if player is either on a snake head
        if positions2[flag] in snake_heads:
            # print(f"Player {p1_name} is in position {p1_position}")
            index = snake_heads.index(positions2[flag])
            positions2[flag] = snake_tails[index]
            print(f"Player {players2[flag]} stepped on a snake and is now in position {positions2[flag]}")

        # Check if player is either on a ladder Base
        if positions2[flag] in ladder_bases:
            # print(f"Player {p1_name} is in position {p1_position}")
            index = ladder_bases.index(positions2[flag])
            positions2[flag] = ladder_tops[index]
            print(f"Player {players2[flag]} climbed a ladder and is now in position {positions2[flag]}")

        if positions2[flag] == 100:
            break

        if positions2[flag] > 100:
            positions2[flag] -= diceroll

        print(f"Player {players2[flag]} is in position {positions2[flag]}")
        flag += 1
i = 0
for i in range(4):
    if positions2[i] == 100:
        winner = winner[i]
        print(f"{winner} has reached 100 and is the winner!")