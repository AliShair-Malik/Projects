import random

computer_number = random.randint(10, 20)

# print(computer_number)

user_number = int(input("Guess the Number betweeb 10 to 20 : "))

while user_number != computer_number:
    user_number = int(input("You are Wrong Please Try Again : "))

print("\nCongratulation You Right Number")