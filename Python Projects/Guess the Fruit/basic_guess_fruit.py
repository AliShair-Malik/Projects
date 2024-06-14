import random

attempts = 0

fruits = ['Watermelon', 'Orange', 'Melon', 'Mango', 'Apple', 'Banana', 'Peach', 'Cherry', 'Pineapple', "Grapes"]

fruit = random.choice(fruits)

# print(fruit)

print("Welcome to Guess the Fruit Game")
print("Can you Guess the Fruit Name\n")
print("Hint: First Letter is Capital")
print(f"Hint: Fruit Length is {len(fruit)}")
user_fruit = input("\nGuess the fruit: ")

while user_fruit != fruit:
    user_fruit = input("You are Wrong Please Try Again : ")
    attempts += 1

    if attempts == 3:
        print(f"\nThe fruit is {fruit}")
        

print("\nCongratulation You Won")
