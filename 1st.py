import random
def hangman():
    words = ["python", "hangman", "coding", "simple", "random"]
    word = random.choice(words)  
    guessed_word = ["_"] * len(word)  
    guessed_letters = []
    attempts_left = 6
    print("Welcome to Hangman!")
    print("Guess the word: ", " ".join(guessed_word))
    while attempts_left > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            print(f"Wrong guess! '{guess}' is not in the word. Attempts left: {attempts_left}")

        print("Current word: ", " ".join(guessed_word))
    if "_" not in guessed_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("😢 Out of attempts! The word was:", word)
hangman()