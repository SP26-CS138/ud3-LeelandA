'''
DEVELOPER(S): Leeland Acuna
COLLABORATOR(S): None
'''
"""
Wordle Recreation: I play wordle almost everyday and I thought it would be a good idea if I were to recreate it


"""

##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
#<replace this line with import statement(s)>
import random

##########################################
# FUNCTIONS:
##########################################
#This function takes the guess input by the user and the word and compares the word inputed by the user and the correct word and returns the result
def guess_word(guess, word):
    result = ""
    for char in range(len(word)):        
        if guess[char] == word[char]:
            result += guess[char]
        
        elif guess[char] in word:
            result += "?"
        
        else:
            result += "_"
    
    return result

#This function gets the words in files
def get_words(filename):
    words = [] #chose to use a list since its easier to randomize a choice of words

    in_file = open(filename, 'r')
    for line in in_file:
        word = line.strip()
        if word != "":
            words.append(word.upper())
    in_file.close()
    return words




##########################################
# MAIN PROGRAM:
##########################################
user_mode = ""

while user_mode != "R" and user_mode != "C":
    user_mode = input("Would you like to play regular wordle or play the challenge mode(R (Regular)/C (Challenge)): ").upper()
    if user_mode == "R":
        words = get_words("wordle.txt")
    elif user_mode == "C":
        words = get_words("challenge.txt")
    else:
        print("Invalid choice.")

word = random.choice(words)
word_letter_amount = len(word)
guess = input(f"Guess the {word_letter_amount} letter word: ").upper()
while guess != word:
    if len(guess) == len(word):
        result = guess_word(guess, word)
        print(result)
        guess = input(f"Guess the {word_letter_amount} letter word:").upper()
    else:
        print("Wrong amount of letters")
        guess = input(f"Guess the {word_letter_amount} letter word:").upper()


print("Congratulations! You got the word!")