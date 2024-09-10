import random

def roll_dice():
    return random.randint(1, 6)

def move_player(player, position):
    dice = roll_dice()
    print(f"Player {player} rolled a {dice}.")
    position += dice
    if position in snakes:
        print(f"Oh no! Player {player} got bitten by a dangerous snake!")
        position = snakes[position]
    elif position in ladders:
        print(f"Great! Player {player} climbed a ladder to safety!")
        position = ladders[position]
    return position

# Snakes and ladders dictionary
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Game setup
player1_position = 0
player2_position = 0
end_position = 100

# Game loop
while True:
    player1_position = move_player("1", player1_position)
    if player1_position >= end_position:
        print("Player 1 wins the dangerous adventure!")
        break
    player2_position = move_player("2", player2_position)
    if player2_position >= end_position:
        print("Player 2 wins the dangerous adventure!")
        break