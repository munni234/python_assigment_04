# find the perpendicular of two right triangle and outputs the length of third side 

#pythagorean theory is used to measure the value of the hypotenuse value of right side traingle.
#In triangle ABC user input the value of the  side of AB and BC and we have to calculate AC.
import math
def main():
    AB_triangle_side = float(input("Enter the side  AB of trinagle: "))
    BC_triangle_side = float(input("Enter the BC side of value of trianlge: "))

    print("""You can find the value of Hypotenus value.
          Using this formula
           a² + b² = c² """)
    
    formula:int = AB_triangle_side ** 2 + BC_triangle_side ** 2
    Hypotenuse = math.sqrt(formula)

    print(f"\nGiven AB = {AB_triangle_side} and BC = {BC_triangle_side},")
    print(f"The length of the hypotenuse AC is: {Hypotenuse:.2f}")



if __name__ == "__main__":
    main()
    