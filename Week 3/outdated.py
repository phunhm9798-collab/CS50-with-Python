# Define a list of months for data verification
list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Define a while loop to repeatedly prompt the user for a date input
# The loop continues until a valid date is provided
while True:
    try:
        date = input("Date:").strip()
        month, day, year = date.split("/")
        if int(day) > 31:
            raise ValueError
        elif int(month) > 12:
            raise ValueError
        else:
            print(f"{year}-{month.rjust(2, "0")}-{day.rjust(2, "0")}")
            break
    except ValueError:
        pass
    try:
        x, y = date.split(",")
        month_1, day_1 = x.split()
        month_1 = str(list.index(month_1)+1)
    except (ValueError, KeyError):
        pass
    else:
        if int(day_1) < 32 and int(month_1) < 13:
            print(f"{y.rjust(4, "0")}-{month_1.rjust(2, "0")}-{day_1.rjust(2, "0")}")
