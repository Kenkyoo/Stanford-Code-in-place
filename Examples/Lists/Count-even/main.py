"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")

    return lst

def count_even(lst):
    count = 0
    for n in lst:
        if n % 2 == 0:
            count += 1
    print(count)
def main():
    lst = get_list_of_ints()
    count = count_even(lst)
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()