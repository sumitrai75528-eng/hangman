import random

words = ["python", "computer", "programming", "developer", "coding"]

word = random.choice(words)

guessed_word = ["_"] * len(word)
wrong_guesses = 0
guessed_letters = []

print(" Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while wrong_guesses < 6 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    
    print("Wrong guesses:", wrong_guesses, "/ 6")

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:import random

words = ["python", "computer", "programming", "developer", "coding"]

word = random.choice(words)

guessed_word = ["_"] * len(word)
wrong_guesses = 0
guessed_letters = []

print(" Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while wrong_guesses < 6 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/ 6")

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print(" Wrong guess!")

if "_" not in guessed_word:
    print("\n You Win!")
    print("The word was:", word)
else:
    print("\n Game Over!")
    print("The word was:", word)
    wrong_guesses += 1
    print(" Wrong guess!")

if "_" not in guessed_word:
    print("\n You Win!")
    print("The word was:", word)
else:
    print("\n Game Over!")
    print("The word was:", word)