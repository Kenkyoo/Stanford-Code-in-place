def main():
    # your code here
    n = int(input("Enter a number: "))
    i = ""
    while n != 1:
        if n % 2 == 1:
            i = f"{n} is odd"
            n = n * 3 + 1
            print(f"{int(i)}, so I make 3n + 1: {int(n)}")
        else:
            i = f"{n} is even"
            n = n / 2
            print(f"{int(i)}, so I take half: {int(n)}")

