#The result of division and the remiander
Bold = "\033[1m"
italic = "\033[3m"

def main():
    first_number = int(input(f"{Bold}{italic} Please enter an integer to be divided: "))
    second_number = int(input(f"{Bold}{italic} Please enter an integer to be divided by: "))

    quotient = first_number / second_number
    remainder = first_number % second_number

    print(f"""The remainder of the division of {first_number} by {second_number} is {remainder}
          and the quotient of these division is {quotient:.2f}""")
    

if __name__ == "__main__":
    main()
