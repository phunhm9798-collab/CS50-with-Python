# Set the base amount of money due
due = 50

# A loop that will output the amount due at the start, then accept currency in the range of 5, 10 or 25
while True:
    print("Amount Due:", due)
    money = int(input("Insert coin:"))
    if money == 5 or money == 10 or money == 25:
        # Then it check if money is still due, if no, then it will output the amount of change owed
        if (money >= due):
            print("Change Owed:", money - due)
            break
        due -= money
    # If there is still due, the loop continues until the conditions are satisfied
    else:
        continue
