def count_even(lst):
      """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
      count = 0
      for i in range(len(lst)):
       num = lst[i]
      
       if num % 2 == 0:
           count += 1

      print(count)

def get_list_of_ints():
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop.: ")
    return lst

def main():
    lst =  get_list_of_ints()
    count_even(lst)


if __name__ == "__main__":
    main()