# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    # TODO: your code here
    for i in range(1, MAX_NUMBER + 1):
        if i & 1:
            print(f"{i} is odd")
        else:
            print(f"{i} is even")

if __name__ == "__main__":
    main()