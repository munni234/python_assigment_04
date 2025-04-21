import random as rd
def main():
   print(*[rd.randint(1, 50) for _ in range(10)])

if __name__ == "__main__":
   main()