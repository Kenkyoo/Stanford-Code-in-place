"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():    
    while True:
        a = int(input("How tall are you? "))
        if a > 100:
            print("You're tall enough to ride!")
            break
        print("You're not tall enough to ride, but maybe next year!")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
