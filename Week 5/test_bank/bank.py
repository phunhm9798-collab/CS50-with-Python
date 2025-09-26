def main():
    greet = input('Greeting: ').lower().strip()
    v = value(greet)
    print(f'${v}')


def value(greeting):
    print(greeting)
    if greeting.startswith('hello'):
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
