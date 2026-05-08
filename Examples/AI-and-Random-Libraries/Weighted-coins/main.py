"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

import random

def main():
    coin = random.choices(["heads", "tails"], weights=[60, 40])[0]
    print(coin)

if __name__ == '__main__':
    main()
