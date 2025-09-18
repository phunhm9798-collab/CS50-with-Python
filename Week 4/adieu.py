# Import the necessary module and define a variable containing it
import inflect
p = inflect.engine()

# Create an empty list to store the user's inputted names
name = []

# Define a loop that prompts the user for a name
# If valid, then it will add it into the above list and continue the loop
# If invalid, then it will print a blank message and break the loop
while True:
    try:
        message = input('Name: ')
    except EOFError:
        print()
        break

    else:
        name.append(message)

# Print the list of available name along with the predetermined message
print(f"Adieu, adieu, to {p.join(name)}")
