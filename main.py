import json
def get_data(key):
    return data[key]
def add_data(key, value):
    data[key] = value
def delete_data(key):
    del data[key]
def menu():
    print("1. Get data")
    print("2. Add data")
    print("3. Delete data")
    print("4. Exit")

if __name__ == "__main__":
    with open('data.json', "r") as f:
        data = json.load(f)
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        key = input("Enter key: ")
        print(get_data(key))
    elif choice == 2:
        key = input("Enter key: ")
        value = input("Enter value: ")
        add_data(key, value)
    elif choice == 3:
        key = input("Enter key: ")
        delete_data(key)
    elif choice == 4:
        exit()
    else:
        print("Invalid choice")
with open('data.json', "w") as f:
    json.dump(data, f)