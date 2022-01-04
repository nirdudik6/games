import random
from time import sleep

def play():
    user=input("choose rock, scissors, paper\n")
    computer=random.choice(['rock','paper','scissors'])

    if user == computer:
        sleep(3)
        print("I chose: " + computer)
        return 'tie'
    if win(user, computer):
        sleep(3)
        print("I chose: " + computer)
        return 'you won!'
    sleep(3)
    print("I chose: " + computer)
    return 'you lost'
def win(user, computer):
    if (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return True

print(play())


