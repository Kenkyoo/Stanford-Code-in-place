import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    for i in range(N_NUMBERS):
        rand_num = random.randint(MIN_VALUE, MAX_VALUE) 
        print(rand_num)
        