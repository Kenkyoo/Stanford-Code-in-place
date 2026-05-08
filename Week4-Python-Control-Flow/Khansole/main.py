import random

def main():
    
    # TODO: your code here
    x = random.randint(10, 99) 
    y = random.randint(10, 99) 
    z = x + y

    q = f"What is {x} + {y}?"

    c = "Correct!"
    i = "Incorrect."
    m = f"The expected answer is {z}"

    khansole(q, z, c, i, m)

def khansole(q, z, c, i, m):
    print("Khansole Academy")
    print(q)
    a = int(input(f"Your answer: "))

    if a == z:
        print(c)
    else:
        print(i)
        print(m)

    
if __name__ == '__main__':
    main()
