# Define a menu with items and their corresponding prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# Set the based cost to zero
total = 0
# Define a while loop to repeatedly prompt the user for an item
# If the item is not on the menu, the loop continues to prompt the user
# If the item is on the menu, the price is added to the total and the total is printed
# If the user signals EOF (control-d), the loop breaks and the program ends
while True:
    try:
        item = input("Item: ").strip().lower().title()
        if item not in menu:
            raise KeyError
    except KeyError:
        continue
    except EOFError:
        print("")
        break
    else:
        total += menu[item]
        print(f"Total : ${total:.2f}")
