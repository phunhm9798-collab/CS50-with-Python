# Get the user's expression
expression = input("Expression:")
# Split the inputted expression into 3 variables
x, y, z = expression.split(" ")
# Calculate the answer based on the inputted expression
if y == "+":
    a = int(x) + int(z)
    print(f"{a:.1f}")
if y == "-":
    b = int(x) - int(z)
    print(f"{b:.1f}")
if y == "*":
    c = int(x) * int(z)
    print(f"{c:.1f}")
if y == "/":
    d = int(x) / int(z)
    print(f"{d:.1f}")
