inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}

item = input("Enter item name: ").strip().lower()

if item in inventory:
    print("Available quantity:", inventory[item])

    sold = int(input("Enter quantity sold: "))

    if sold <= 0:
        print("Please enter a quantity greater than 0.")

    elif sold > inventory[item]:
        print("Not enough stock available.")

    else:
        inventory[item] -= sold

        if inventory[item] == 0:
            del inventory[item]

        print("Sale recorded successfully.")
else:
    print("Item not found in inventory.")

print("Updated inventory:", inventory)