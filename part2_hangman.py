# load a text file and make words a list
with open('words.txt') as f:
    all_words = f.readlines()

# words = [w.strip() for w in all_words] # list compreshen

words = []
for w in all_words:
    words.append( w.strip() )

print(words)
import random 
myword = random.choice(words)
guess = len(myword) * ["_"]

chances = 10
while chances>0:
    print('you have chances left',chances)
    print(guess)
    g = input('enter your chracter!: ')
    for i,v in enumerate(myword): # check the word letter by letter
        if g ==v:
            guess[i] = g # if character/letter is matching then fill the blanks
            chances = chances + 1
    # if all spaces are filled close game
    if "_" not in guess:
        break

    


    chances = chances - 1

print('so words was',myword)