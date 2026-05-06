def main():
    prompt = "What do you want? "
    user_input = input(prompt)
    # your code here.
    joke = "Here is a joke for you! Karel is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Karel returns with 13 liters of milk. The programmer asks why and Karel replies: 'because they had eggs'"
    sorry = "Sorry I only tell jokes"

    if user_input == "Joke":
        print(joke)
    else:
        print(sorry)


if __name__ == "__main__":
    main()
