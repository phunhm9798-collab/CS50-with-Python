# Import the necessary modules
from pyfiglet import Figlet
import sys
from random import choice

# Define figlet as a variable(Somehow it doesn't work when used sepparately)
figlet = Figlet()
font_list = figlet.getFonts()

# Define a loop that will choose a random font for the user's input based on the command line argument length
if len(sys.argv) == 1:
    random = choice(font_list)
    figlet.setFont(font=random)


# Define a loop that will choose a specific font for the user's input based on the command line argument length
elif len(sys.argv) == 3:
    specific = sys.argv[2]
    font_position = sys.argv[1]
    if font_position == "-f" or font_position == "--font" and specific in font_list:
        figlet.setFont(font=specific)
    else:
        sys.exit("Invalid usage")

# Output a message in case of a invalid input
else:
    sys.exit("Invalid usage")

# Get the user's input
message = input("Input: ")

# Output the altered message
print("Output:", figlet.renderText(message), sep="\n")
