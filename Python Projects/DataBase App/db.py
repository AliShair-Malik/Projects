import json

while True:
    db_name = input("Enter Your DataBase Name: ").lower()
    ans = input(f"Are you Sure the DB name is \'{db_name}\' (y/N): ")

    if ans == "y" or ans == "Y":
        break

def data_base():
    try:
        with open(f"{db_name}.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(f"{db_name}.txt", "w") as file:
        json.dump(data, file)

def create_collection(data):
    while True:
        collection_name = input("Enter the Collection Name: ").lower()
        ans = input(f"Are you Sure the Collection Name is \'{collection_name}\' (y/N): ")

        if ans == "y" or ans == "Y":
            break

    data[collection_name + "s"] = {}
    save_data(data)

def access_the_collection(data):
    def insert_data(data):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        data[choice][key] =  value
        save_data(data)

    def show_data(data):
        if not data[choice]:
            print("There is nothing Insert the Data")
        else:
            print("Data:")
            for key, value in data[choice].items():
                print(f"{key}: {value}")

    def update_data(data):
        show_data(data)
        key = input("\nEnter the Data which is you need to Update: ")

        if not data[choice]:
            print("There is Nothing Insert a Data")
        elif key not in data[choice]:
            print("Invalid Input")
        else:
            value = input(f"Enter the new value to the {key}: ")
            data[choice][key] = value
            save_data(data)

    def delete_data(data):
        show_data(data)
        key = input("Which you need to Delete: ")

        if not data[choice]:
            print("There is Nothing Insert a Data")
        elif key not in data[choice]:
            print("\nInvalid Input")
        else:
            del data[choice][key]
            save_data(data)
                

    def data_access():
        while True:
            print("\n1. Insert the Data")
            print("2. Show all Data")
            print("3. Update the Data")
            print('4. Delete the Data')
            print("5. Quit the App")
            choice = input("Enter Your Chioce: ")

            match choice:
                case "1":
                    insert_data(data)
                case "2":
                    show_data(data)
                case "3":
                    update_data(data)
                case "4":
                    delete_data(data)
                case "5":
                    print("\nYou SucessFuly Quit the App")
                    break
                case _:
                    print("Invalid Input")

                
    if not data:
        print("\nThere is Nothing Create a Collection")
    else:
        print("\nWhich Collection need you to perform a CRUD opration")
        for collectons in data.keys():
            print(collectons)

        choice = input("Enter the Collection Name which you need to Access: ")

        if choice in data:
            data_access()
        else:
            ("\nInvalid Input")


def delete_collection(data):
    collection_name = input("Enter the Collection Name Which You Delete: ")

    if collection_name in data:
        del data[collection_name]
    else:
        print("No Collcetion Found")
    
    save_data(data)

def main():
    data = data_base()
    print("\nWelcome to Python DataBase")

    while True:
        print(f"You are in {db_name} DB\n")
        print("1. Create a Collectoin")
        print("2. Enter the Exist Collection")
        print("3. Delete a Collaction")
        print("4. Quit a DataBase")
        choice = input("Enter your Choice: ")

        match choice:
            case "1":
                create_collection(data)
            case "2":
                access_the_collection(data)
            case "3":
                delete_collection(data)
            case "4":
                print("\nYou SucessFuly Quit the App")
                break
            case "5":
                print("Invalid Input")


if __name__ == "__main__":
    main()
