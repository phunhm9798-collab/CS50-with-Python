# Define a while loop to repeatedly prompt the user for a valid fraction input
# The loop continues until a valid fraction is provided
# If a valide fraction is provided, the loop breaks and the programs continues
while True:
    fuel_amount = input("Fraction: ")
    x, y = fuel_amount.split("/")
    try:
        if y == 0:
            raise ZeroDivisionError
        if int(x) < 0 or int(y) < 0:
            raise ValueError
        percent = (int(x) / int(y)) * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if int(x) <= int(y):
            break

# Output the fuel percentage based on the user's input
if percent >= 99:
    print("F")
elif percent <= 1:
    print("E")
else:
    print(f"{percent:.0f}%")
