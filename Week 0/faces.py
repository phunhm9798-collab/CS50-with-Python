# Define a fuction that gets the user's message, call a function to convert it, then print the converted message
def main():
    message = input("What is your message?")
    msg = convert(message)
    print(msg)

# Define a fuction that convert the user message when called


def convert(message):
    converted = message.replace(":)", "🙂").replace(":(", "🙁")
    return converted


main()
