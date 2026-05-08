def main():
    """
    You should write your code here. 
    """
    stones = 20

    player = 1

    while stones > 0:
        m = print(f"There are {stones} stones left.")
        a = int(input(f"Player {player} Would you like to remove 1 or 2 stones? "))

        while a < 1 or a > 2:
             a = int(input("Please enter 1 or 2: "))
        
        stones -= a
        
        if stones > 0:
            player = 2 if player == 1 else 1

    winner = 2 if player == 1 else 1
    print(f"Player {winner} wins!")

if __name__ == '__main__':
    main()
