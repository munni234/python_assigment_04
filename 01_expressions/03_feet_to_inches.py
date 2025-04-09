#converts feet to inches.

print("Put the value in input to convert it into inches")

def main():
    user_input_infoot = float(input("Enter the number of foot: "))
    print("One foot is equal to 12 inches")
    res = user_input_infoot * 12
    print(f"{user_input_infoot} foot or feet is equal to {res} inches")



if __name__ == "__main__":
    main()