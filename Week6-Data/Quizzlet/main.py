def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    count = 0
    for key, value in translations.items():
        a = input(f"What is the Spanish translation for {key}? ")
        if a == value:
            print("That is correct!")
            count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {key} is {value}.")
    print(f"You got {count}/{len(translations)} words correct, come study again soon!")
    
if __name__ == '__main__':
    main()