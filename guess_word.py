import random
from time import sleep
name = input("Enter your name:\n")
print("Hello "+name +"!")
print("good luck!")
sleep(2)
words = ['nir', 'eitan', 'ron', 'tzioni', 'yogev', 'dor', 'niv shalom', 'niv nissim', 'bar shemesh', 'idan moshe', 'amit', 'noam', 'bobi', 'eden', 'meidan', 'yuval', 'agam', 'moti', 'ilanit', 'dasha' , 'sasha']
word = random.choice(words)
print("guess the name!!")
turns = 10
display = "_"*len(word)
game_over=False

while not game_over:
    print("you have "+ str(turns) + " left!")
    print(display)
    guess = input("please guess a letter: ")

    i = 0

    if guess in word:
        while word.find(guess, i ) != -1:
            i = word.find(guess, i)
            display = display[:i] + guess + display[i +1:]
            i += 1
        print("correct!")
    else:
        print("sorry wrong guess!")
        turns -= 1
    if word == display:
        print("you win! the word is " + word)
        game_over = True
    if turns == 0:
        print("sorry you ahve lost :( ")
        game_over = True