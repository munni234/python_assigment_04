def main():
     fruits = {"apple":200, "mango": 150 , "banana": 300 , "grapes": 400}

     total_cost = 0

     for key, val in fruits.items():
      price = val
      amount_bought = int(input("How many (" + key +" ) do you wnat to buy?: "))
      total_cost += (price * amount_bought)

     print("Your total is $" + str(total_cost))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
