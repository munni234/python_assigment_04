#mutable


def add_three_copies(datalist, data):
    for i in range(3):
        datalist.append(data)
    


def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before: ", my_list)
    add_three_copies(my_list, message)
    print("before: ", my_list)


if __name__ == "__main__":
    main()
