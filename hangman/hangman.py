import random

def dashes(word, guesses):
    dash = ""
    for letter in word:
        if letter in guesses:
            dash = dash + letter
        else:
            dash = dash + "_"
    return dash

file = open("words_alpha.txt").read().split()
allowedWords = [wrd for wrd in file if len(wrd) < 6]
word = random.choice(allowedWords)
guesses = []
tries = 6
while tries > 0:
    newWord = dashes(word,guesses)
    if "_" not in newWord:
        break
    print(newWord)
    guess = input("Previous guesses: " + str(guesses) + "\nGuess a letter: ")
    guesses.append(guess)
    if guess not in word:
        tries = tries - 1
        print(tries,"bad guesses left")
print(word)