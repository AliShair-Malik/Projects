import random

attempts = 0

fruits = ['Watermelon', 'Orange', 'Melon', 'Mango', 'Apple', 'Banana', 'Peach', 'Cherry', 'Pineapple', "Grapes"]

fruit = random.choice(fruits)

print("Welcome to Guess the Fruit Game")
print("Can you Guess the Fruit Name\n")
print("Hint: First Letter is Capital")
print(f"Hint: Fruit Length is {len(fruit)}")
print("\nYou have Only 3 Attempts")
user_fruit = input("\nGuess the fruit: ")

while user_fruit != fruit:
    attempts += 1
    
    if attempts == 3:
        print("You have no More Attempts")
        option = input("Try Again (Yes/NO): ")
        if option == "Yes":
            attempts = -1
        else:
            break
    else:
        user_fruit = input("You are Wrong Please Try Again : ")


if user_fruit == fruit:
    print("\nCongratulation You Win !!")
else:
    print("\nYou loose")

