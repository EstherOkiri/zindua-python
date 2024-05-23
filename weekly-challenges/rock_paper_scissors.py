def game(user_input,comp_input):
    if user_input == comp_input :
        print("Draw")
    elif user_input == 'rock' & comp_input == 'paper':
        print('Computer Wins!')
    elif user_input =='rock' & comp_input == 'scissors':
        print('You Win!')
    elif user_input == 'paper' & comp_input == 'rock' :
        print('You Win!')
    elif user_input == 'paper' & comp_input == 'scissors':
        print('Computer Wins')
    elif user_input == 'scissors' & comp_input == 'rock' :
        print ('Computer Wins')
    elif user_input == 'scissors' & comp_input == 'paper':
        print('You Win!')
    else:
        print('Try Again')

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])