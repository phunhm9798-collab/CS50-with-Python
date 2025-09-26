def main():
    while True:
        try:
            percentage = convert(input('Fraction: '))
        except:
            pass
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0:
        raise ValueError
    return x/y * 100


def gauge(percent):
    if percent >= 99:
        return 'F'
    elif percent <= 1:
        return 'E'
    else:
        return f"{percent:.0f}%"


if __name__ == "__main__":
    main()
