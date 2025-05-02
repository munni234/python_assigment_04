def average(a:float, b:float):
    """
    Returns the number which is half way between a and b 
    """
    sum = a + b
    n = 2
    return sum / n

def main():
        avg_one = average(1, 30)
        ave_two = average(5, 10)
        final = average(avg_one, ave_two)
        print("averageOne", avg_one)
        print("averageTwo", ave_two)
        print("final", final)

if __name__ == "__main__":
      main()