import random
NUM_PAIRS = 3

def main():
    truth = []
    truth_view = []
    
    for i in range(NUM_PAIRS):
        truth.append(i)
        truth.append(i)
        
    random.shuffle(truth)
    
    for i in range(len(truth)):
        truth_view.append('*')
    
    def get_valid_index(displayed_list):
        while True:
            user_input = input("Enter an index: ")
            if not user_input.isdigit() and not (user_input.lstrip('-').isdigit()):
                print("Not a number. Try again.")
                continue
            index = int(user_input)
            if index < 0 or index >= len(displayed_list):
                print("Invalid index. Try again.")
                continue
            if displayed_list[index] != '*':
                print("This number has already been matched. Try again.")
                continue
            return index

    def get_two_indices(displayed_list):
        index1 = get_valid_index(displayed_list)
        while True:
            index2 = get_valid_index(displayed_list)
            if index2 == index1:
                print("You entered the same index twice. Try again.")
            else:
                break
        return index1, index2
    
    while '*' in truth_view:
        print(truth_view)
        index1, index2 = get_two_indices(truth_view)
        if truth[index1] == truth[index2]:
            truth_view[index1] = truth[index1]
            truth_view[index2] = truth[index2]
            print("Match!")
        else:
            print(f"Value at index {index1} is {truth[index1]}")
            print(f"Value at index {index2} is {truth[index2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")
            clear_terminal()

    print(truth_view)
    print("Congratulations! You won!")

def clear_terminal():
    for i in range(20):
        print('\n')

if __name__ == '__main__':
    main()