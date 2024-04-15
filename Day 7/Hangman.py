import random as ran

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
==========
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
==========
''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
==========
''', '''
  +---+
  |   |
  0   |
 /|   |
      |
      |
==========

''', '''
  +---+
  |   |
  0   |
 /    |
      |
      |
==========

''', '''
  +---+
  |   |
  0   |
      |
      |
      |
==========
''', '''
  +---+
  |   |
      |
      |
      |
      |
==========
''']

# Picking a random words and checking Answers
word_list = ["aardvark", "baboon", "camel"]
lives = 6
chosen_word = ran.choice(word_list)

print(f"Pssst, the random word is {chosen_word}")
display = ["_"] * len(chosen_word)
print(''.join(display))
count = 0
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = chosen_word[position]
    else:
        lives -= 1
    print(stages[lives])
    if lives == 0:
        end_of_game = True
        print("You lose")
    print("".join(display))
    if "_" not in display:
        end_of_game = True
        print("You win")
