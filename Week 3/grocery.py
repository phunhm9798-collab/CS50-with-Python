# Initailize an empty list to store the fruits
list = []

# Define a while loop to repeatedly prompt the user for fruit input
# If the user signals EOF (control-d), the loop breaks and the program ends
while True:
    try:
        fruit = input().upper()
    except EOFError:
        print("")
        break
    else:
        list.append(fruit)

# Sort the list of fruits in alphabetical order
list.sort()

# Initialize a counter to track each fruit
k = 0

# Loop through the list of fruits and count the occurrences of each fruit
# If the fruit is the same as the previous fruit, the counter increments
for a in list:
    count = 0
    if k == 0 or list[k] != list[k-1]:
        if list[k] != list[-1]:
            b = k
            while list[b] == list[b + 1]:
                count += 1
                b += 1
        elif len(list) == 2 and list[k] == list[k - 1]:
            count += 1
        print(count+1, a)

    k += 1
