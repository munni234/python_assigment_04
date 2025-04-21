MAX_LENGTH : int = 2

def get_lst():
    """ prompts the user to enter one element of the list at a time and returns the resulting list. """

    lst = []
    elem = input("PLease enter one element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("PLease enter an elemnt of the list or press enter to stop. ")
    return lst
    
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        print(lst)
        last_elemnt = lst.pop()
        print(last_elemnt)


def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()