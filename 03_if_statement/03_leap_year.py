def leap_year():
    year = int(input("Enter year to check "))

    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(year, "leap year")
    else:
        print(year, "not a leap year")


def main():
    leap_year()


if __name__ == "__main__":
    main()