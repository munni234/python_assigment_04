def get_last_element():

    lst = []
    element:str = input("Please enter an element of the list at a time or press enter to stop. ")

    while element != "" :
        lst.append(element)
        element = input("Please enter elemnt: ")

    print(lst[-1])
    return lst

    
        
def main():
    get_last_element()

if __name__ == "__main__":
    main()