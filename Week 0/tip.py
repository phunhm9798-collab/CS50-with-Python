# Define a function that gets the user's inputs, calculate the tip, and output the results
def main():
    dollars = dollars_to_float(input("How much was the meal?"))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = int(dollars) * float(percent)
    print(f"Leave ${tip:.2f}")

# Define a function that converts inputted meal price into a float


def dollars_to_float(d):
    # TODO
    d = d.strip("$")
    d = float(d)
    d = round(d, 2)
    return d

# Define a function that converts inputted tip percentage into a float


def percent_to_float(p):
    # TODO
    p = p.strip("%")
    p = float(p) / 100
    p = round(p, 2)
    return p


main()
