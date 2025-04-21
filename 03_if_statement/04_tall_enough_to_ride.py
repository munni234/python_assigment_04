MINIMUM_LENGTH: int = 50

def main():
    height:int = float(input("How tall are you? "))

    if height <= MINIMUM_LENGTH:
        print("you are not enough tall to ride.")
    else:
        print("you are tall to ride.")


if __name__ == "__main__":
    main()