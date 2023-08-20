import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
chosen_word = random.choice(word_list)
guess = input("Enter a guess:")
blanks = len(chosen_word)
word = []
x = 0
for i in range(blanks):
  word.append("_")
blanks += 5
while blanks > 0:
  for i in chosen_word:
    x += 1
    if i == guess:
      word[x-1] = guess
    else:
      continue
  print(word) 
  guess = input("Enter a guess:")
  x = 0
  blanks -= 1
  for y in word:
    if y == "_":
      j = 1
    else:
      j = 0
      continue
print(word)      
if j == 1:
  print("YOU LOSE!")
else:
  print("YOU WIN!")