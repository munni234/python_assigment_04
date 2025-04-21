#voting age in stanlau is 25
#voting age in mayengua is 48
#peturksbouipo is 16

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
 
    print("""
    You can vote for the following three countries:
    1. Peturksbouipo (Age 16)
    2. Stanlau (Age 25)
    3. Mayengua (Age 48)
    """)
    user_age : int = int(input("Enter you age: "))
    choice = input("Enter 1, 2, or 3: ")

    match choice:
        case "1":
           if user_age >= STANLAU_AGE:
            print("You can vote for stanlau")
           else:
              print("you are not old enough to vote for stanlau.")
        case "2":
           if user_age >= PETURKSBOUIPO_AGE:
            print("You can vote for 'PETURKSBOUIPO_AGE' ")
           else:
              print("you are not old enough to vote for Peturksbouipo.")
        case "3":
            if user_age >= MAYENGUA_AGE:
               print("you can vote for MAYENGUA_AGE ")
            else:
               print("you are not old enough to vote for MAYENGUA_AGE.")

        case _:
          print("Invalid choice.")


if __name__ == "__main__":
   main()