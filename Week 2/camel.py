# Get the user's input and define the base output
name = input("camelCase:")
output = ""
# Converts the user's input based on different cases
for char in name:
    if char.isupper():
        output += "_" + char.lower()
    else:
        output += char
print("snake_case:", output)
