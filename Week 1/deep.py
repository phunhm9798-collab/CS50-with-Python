# Get the user's input
answer = input(
    "What is the Answer to the great question of Life, the Universe, and Everything?").lower().strip()

# Output answer for different cases
if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two" or answer == "Forty Two":
    print("Yes")
else:
    print("No")
