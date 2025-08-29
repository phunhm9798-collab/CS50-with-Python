# Define a function that get the user's time and make decision based on it
def main():
    time = input("What time is it?")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# Define a function that split inputted time into hour and minutes, then convert it into desirable form


def convert(time):
    hour, minutes = time.split(":")
    if int(minutes) >= 0:
        minutes = int(minutes) / 60
        time = int(hour) + minutes
        return round(time, 2)


if __name__ == "__main__":
    main()
