# simulate rolling two dice and prints the results of each roll as well as as the toatal.
import random as rd
def main():
    roll_dice = 6

    die_one:int = rd.randint(1, roll_dice)
    die_two:int = rd.randint(1, roll_dice)

    total:int = die_one + die_two

    print("Dice have", roll_dice, "sides each.")
    print("First die:", die_one)
    print("Second die:", die_two)
    print("Total of two dice is:", total)


if __name__ == "__main__":
    main()

