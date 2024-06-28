import random
import os 

computer_turn = None
user_turn = None
computer_score = 0
user_score = 0
options = ['Rock', 'Paper', 'Scissor']


while user_score != 10 or computer_score != 10:
    computer_turn = random.choice(options)
    
    print("Rock,Paper,Scissor\n")    
    print("Who First Get 10 Points his Win\n")
    
    
    print("\nYour Turn")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    option = input("\nEnter Your Choice: ")

    match option:
        case "1":
            user_turn = 'Rock'
        case "2":
            user_turn = 'Paper'
        case "3":
            user_turn = 'Scissor'
        case _:
            print('Invalid Input')

    print(f'\nYour Choice is {user_turn}')
    print(f'Computer Choice is {computer_turn}\n')


    if user_turn != computer_turn:
        if option == 'Rock' and computer_turn == 'Scissor':
            user_score += 1
            print("Your Score:", user_score)
            print("Computer Score:", computer_score)
        elif option == 'Scissor' and computer_turn == 'Rock':
            computer_score += 1
            print("Your Score:", user_score)
            print("Computer Score:", computer_score)
    else:
        print('This is Draw\n')




    
        



