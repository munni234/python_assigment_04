def double(num:int):
    return num * 2

def main():
    num = int(input("Enter a number: "))
    num_two_times = double(num)
    print("Double that is ", num_two_times)

if __name__ == "__main__":
    main()