import random
DONE_LIKELIHOOD = 0.3

def chaotic_counting():
    for i in range(10):
        current_num = i + 1
        if done():
            return
        print(current_num, "loop i")



def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I am counting")
    chaotic_counting()
    print("I am done")

if __name__ == "__main__":
    main()
        