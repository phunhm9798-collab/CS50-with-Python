# Get the user's greeting
greeting = input("Greeting:").lower().strip()

# Output value for different cases
if "hello" in greeting:
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
