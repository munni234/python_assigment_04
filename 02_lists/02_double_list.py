def double_numbers(num):
    new_list = []
    for i in num:
        new_list.append(i * 2)
        
    return new_list

def main():
    number_list:list[int] = [1, 22, 4, 3, 65]
    print(double_numbers(number_list))


if __name__ == "__main__":
    main()