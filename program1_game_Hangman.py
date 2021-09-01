#Game Hangman
#The user needs to be able to input letter guesses.
#There needs to be a limit on how many guesses they can use. (To keep things simple pick 3?) 
#Keep notifying the user of the remaining turns.

# pip install RandomWords
from random_words import RandomWords

rw = RandomWords()
word = rw.random_word()
# start part and get the user's name
name = input("What is your name? ")
print("Good luck ! " + name)
print("Guess the characters")
leng = len(word)  # get the length of the word and decide how many "_" should be

for each in range(0, leng):  # print the "_"s
    print("_")
guess_word = ["_"] * leng  # store the word user are guessed
i = 5  # have 5 loops while 3 loops is hard to reach correct answer
while True:
    guess_words = guess_word.copy()
    x = input("guess a character:")
    k = 0
    # check and turn the character which is true and load that to guess word.
    for each in word:
        if each == x:
            guess_word[k] = x
        k += 1
    # When the user enters the correct word, print"congratulations"
    if guess_word == list(word):
        print("Congratulations!")
        break
    # when guess word did not change means user printed a wrong character
    if guess_words == guess_word:
        i -= 1
        # when i==0 means user used all tries, program will break
        if i == 0:
            break
        print("Wrong")
        print("You have " + str(i) + " more guesses")
    for each in guess_word:
        print(each)  # print the guess word
print("Right word is " + word)  # The correct word will given at the last of the program.
