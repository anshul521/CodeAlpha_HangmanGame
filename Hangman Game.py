import random

# Predefined list of words
word_list = ['apple', 'zebra', 'grape', 'mango', 'lemon']
chosen_word = random.choice(word_list)

# Game state
guessed_letters = []
correct_letters = ['_' for _ in chosen_word]
remaining_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

while remaining_guesses > 0 and '_' in correct_letters:
    print("Word:", ' '.join(correct_letters))
    print("Guessed letters:", ' '.join(guessed_letters))
    print(f"Remaining incorrect guesses: {remaining_guesses}")

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!\n")
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                correct_letters[i] = guess
    else:
        print("❌ Wrong guess!\n")
        remaining_guesses -= 1

# End game message
if '_' not in correct_letters:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game over! The word was:", chosen_word)
