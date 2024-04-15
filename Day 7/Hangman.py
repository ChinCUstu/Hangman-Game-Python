import random as ran

# Picking a random words and checking Answers
word_list = ["aardvark", "baboon", "camel"]

chosen_word = ran.choice(word_list)

print(f"Pssst, the random word is {chosen_word}")
display = ["_"] * len(chosen_word)
print(''.join(display))
guess = input("Guess a letter: ").lower()
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display[i] = chosen_word[i]
    # else:
    #     print("Nope")
print(''.join(display))
