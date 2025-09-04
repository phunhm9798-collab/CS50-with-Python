# Define a function that get the user's input, remove any spaces or special symbols
# And check if the inputted plate number is valid
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Define a function that checks the conditions for a valid plate


def is_valid(s):
    if 1 < len(s) < 7 and s[0:2].isalpha() and s.isalnum() and check_middle_number(s):
        return True

# Define a function that checks the positioning of symbols on the inputted plate


def check_middle_number(s):
    x = 0
    # check from the back to see if any number comes before an alphabetical symbol
    for i in range(3):
        if s[(len(s)-1)-i].isalpha():
            if s[(len(s)-i-1)-1].isnumeric():
                x += 1
    if x > 0:  # means that numbers are in the middle of the plate
        return False
    if x == 0:  # check if the first number is a zero
        for j in range(len(s)-1):
            if s[j].isalpha():
                if s[j+1] == "0":
                    return False
    return True


main()
