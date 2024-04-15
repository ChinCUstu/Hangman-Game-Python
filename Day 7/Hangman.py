import random as ran

import hangman_art as art
import hangman_words as words

print(art.logo)

chosen_word = ran.choice(words.word_list)
count = 0

lives = 6
end_of_game = False

print(f"Pssst, the random word is {chosen_word}")
display = ["_"] * len(chosen_word)
print(''.join(display))
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = chosen_word[position]
    else:
        lives -= 1
        print(art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose")
    print("".join(display))
    if "_" not in display:
        end_of_game = True
        print("You win")
