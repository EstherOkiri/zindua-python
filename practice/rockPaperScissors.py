import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options :
    player = input("Enter a choice(rock,paper,scissors): ")

print(f"Player : {player}")
print(f"Computer : {computer}")

if player == computer:
    print("Its a Draw!")
elif player == "rock" and computer == "scissors":
    print("You Win!")
elif player == "rock" and computer =="paper":
    print("Computer Wins!")
elif player == "paper" and computer == "rock":
    print("You Win!")
elif player == "paper" and computer == "scissors":
    print("Computer Wins!")
elif player == "scissors" and computer == "rock":
    print("Computer Wins!")
else :
    print("You Win!")
