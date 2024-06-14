import json

def load_data():
    try:
        with open("food_list.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_food(foods):
    with open("food_list.txt", "w") as file:
        json.dump(foods, file)

def owner():
    foods = load_data()

    def show_foods(foods):
        for food, price in foods.items():
            print(f"{food} Rs.{price}")

    def add_food(foods):
        name = input("Enter the Food Name: ")
        price = int(input("Enter the Food Price: "))
        foods[name] = price
        save_food(foods)

    def update_food_price(foods):
        show_foods(foods)
        name = input("Enter the Food Name: ")

        if name in foods:
            price = int(input("Enter the New Food Price: "))
            foods[name] = price
            print("Update Successfuly")
            save_food(foods)
        else:
            print("Invalid Input")

    def delete_food(foods):
        show_foods(foods)
        name = input("Enter the Food Name: ")

        if name in foods:
            del foods[name]
            print("\nDelete Successfuly")
            save_food(foods)
        else:
            print("Invalid Input")


    while True:
        print("\nThis is your Instructions\n")
        print("1. Show All the Foods")
        print("2. Add the Food")
        print("3. Update the Food Price")
        print("4. Delete the Food")
        print("5. Exit")
        choice = input("Enter the Choice: \n")

        match choice:
            case "1":
                show_foods(foods)
            case "2":
                add_food(foods)
            case "3":
                update_food_price(foods)
            case "4":
                delete_food(foods)
            case "5":
                print("You Successfuly Exit the Restaurant")
                break
            case _:
                print("Invalid Input")

def customer():
    total_price = 0
    foods = load_data()

    print("\nSir This is The Meun\n")
    for food, price in foods.items():
        print(f'{food} Rs.{price}')

    food = input("\nSir What is your Order: ")

    if food in foods:
        total_price += foods[food]

    option = input("\nDo you need other Order(Yes/No): ")
    
    while option == "Yes" or option == "Y" or option == "y":
        food = input("\nSir What is your Order: ")

        if food in foods:
            total_price += foods[food]

        option = input("\nDo you need other Order(Yes/No): ")

    print(f"\nSir This Your Total Amount is {total_price}")

def main():
    print("Welcome to Python Restaurant\n")
    print("Who are You ?")
    print("1. I am Customer")
    print("2. I am Owner of this Restaurant")
    print("3. Exit the Restaurant")
    choice = input("Who are You: ")

    match choice:
        case "1":
            customer()
        case "2":
            owner()
        case "3":
            print("You Successfully Exit the Restaurant")
        case _:
            print("Invalid Input")

if __name__ == "__main__":
    main()