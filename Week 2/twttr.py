# Define a function that gets the user's input and set the default output
def main():
    text = input("Input: ")
    output = ""
# Check if there is a vowel present in the inputted message
# If yes, the function will clear it. If no, the message remains unchanged
    for a in text:
        if not_a_vowel(a):
            output += a
    print(f"Output: {output}")


# Define a function that identifies vowels (case insensitively)
def not_a_vowel(b):
    if b not in "aeiouAEIOU":
        return True


main()
