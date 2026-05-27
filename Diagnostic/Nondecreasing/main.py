def main():
    print("Enter a sequence of non-decreasing numbers.")
    
    lst = []
    
    lst.append(float(input("Enter num: ")))
    
    while True:
        n = float(input("Enter num: "))
        
        if n >= lst[-1]:
            lst.append(n)
        else:
            break
    
    print("Thanks for playing!")
    print(f"Sequence length: {len(lst)}")
    
if __name__ == "__main__":
    main()