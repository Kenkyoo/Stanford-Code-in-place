def main():
    """
    You should write your code here. 
    """
    curr_value = int(input("Enter a number: "))
    double_it(curr_value)

def double_it(n):
    while n < 100:
        n = n * 2
        print(n)

if __name__ == '__main__':
    main()
