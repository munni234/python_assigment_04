""" Prints the first element of a provided list. """

def get_first_element(lst):
     print("full basket is:",lst)
     print("first thing of basket is: ",lst[0])

def get_list():
     """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
     
     lst = []
     element:str = input("Please enter an element of the list or press enter to stop.")
    

     while element != "":
         lst.append(element)
         element:str = input("Please enter an element of the list or press enter to stop.")

     return lst


def main():
     lst = get_list()
     get_first_element(lst)


if __name__ == "__main__":
     main()
