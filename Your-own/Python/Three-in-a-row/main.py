import random

def main():
    
    # TODO: your code here
    s = 0
    while s < 3:
        s = khansole(s)
    print("Congrats!")

def khansole(s):
    x = random.randint(1, 9) 
    y = random.randint(1, 9) 
    z = x + y
    
    q = f"What is {x} + {y}?"

    c = "Correct!"
    i = "Incorrect."
    m = f"The expected answer is {z}"
    print("Khansole Academy")
    print(q)
    a = int(input(f"Your answer: "))

    if a == z:
        print(c)
        s += 1
        print(f"You score: {s}")
        return s
    else:
        print(i)
        print(m)
        s = 0
        print(f"You score: {s}")
        return s

    
if __name__ == '__main__':
    main()
