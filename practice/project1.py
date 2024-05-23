import random
#Pig
#Allow user to roll a dice - Generation a random number
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

#number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4 :
            break
        else:
            print ("Must be between 2 - 4 players")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

#player turns
while max(player_scores) <max_score:
    should_roll = input()