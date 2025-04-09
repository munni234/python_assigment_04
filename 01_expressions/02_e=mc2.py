#Get a value from the user and then outputs the equivalent energy using eintein formula 

c = 299792458

Bold = "\033[1m"
italic = "\033[3m"



def main():
    mass_in_kg = float(input(f"{italic} {Bold} Enter kilos of mass: "))

    energy = mass_in_kg * (c ** 2)

    print("e = m * c ^ 2...")

    print("m" + str(mass_in_kg) + "kg")
    print("C = " + str(c) + "m/s")

    print(str(energy) + "joules of energy!")


if __name__ == "__main__":
    main()
