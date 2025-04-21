def add_any_number(number):
    """ Takes in a list of numbers and returns the sum of those numbers. """

    total_number = 0
    for i in number:
        total_number  += i
        
        

    return total_number

def main():
    number = [1, 33, 5, 999]
    print(type(number))
    sum_of_numbers = add_any_number(number)
    print(sum_of_numbers)


if __name__ == "__main__":
    main()