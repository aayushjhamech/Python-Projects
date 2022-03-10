# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random
import qrcode


def operations(i, j, l):
    add = i + j;
    multiplication = i * j
    division = (i * j) / l
    print(add, multiplication, division)


def qrGen():
    img = qrcode.make("www.youtube.com")
    img.save("youtube.jpg")


def numberGame(lower, upper):
    x = random.randint(lower, upper)
    tries = round(math.log(upper - lower + 1, 2))
    print("You have ", tries, "tries")

    count = 0;
    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = (int)(input("Guess a number-- "))

        if x > guess:
            print("Incorrect! The number you guessed is too small!!")

        elif x < guess:
            print("Incorrect! The number you guessed is too big!!")
        elif x == guess:
            print("You did it in ", count, "tries")

    if count > tries:
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")


def choose():
    words = ['rainbow', 'computer', 'science', 'programming',
             'mathematics', 'player', 'condition', 'reverse',
             'water', 'board']
    pick = random.choice(words)
    return pick


def jumble(word):
    random_word = random.sample(word, len(word))
    # joins different strings like '.'.join("ab", "cd", "ef") --->> ab.cd.ef
    jumbled = ''.join(random_word)
    return jumbled


def thank(p1name, p2name, pp1, pp2):

    pass


def play():

    #Names of players
    p1name= input("Enter Player 1 name: ")
    p2name= input("Enter Player 2 name: ")

    #Scores of players
    pp1=0
    pp2=0

    #turn counter
    turn=0

    while True:

        chosen = choose()
        jumbled = jumble(chosen)
        print("Jumbled word is: ", jumbled)

        if turn%2 ==0:
            print(p1name, ", it's your turn")
            ans= input("What's the answer? ")

            if ans== chosen:
                pp1+=1

                print("Your score: ", pp1)
                turn+=1
            else:
                print("Better luck next time!")
                print(p2name, ", it's your turn")
                ans = input("What's the answer? ")
                if ans == chosen:
                    pp2 += 1
                    print("Your score: ", pp2)
                else:
                    print("Better luck next time.... Correct workd is: ", chosen)

                c= (int)(input("Press 1 to Continue or 0 to Quit"))
                if c==0:
                    thank(p1name, p2name, pp1, pp2)
                    break
        else:
            print(p2name, ", it's your turn")
            ans = input("What's the answer? ")

            if ans== chosen:
                pp2+=1

                print("Your score: ", pp2)
                turn+=1
            else:
                print("Better luck next time!")
                print(p1name, ", it's your turn")
                ans = input("What's the answer? ")
                if ans == chosen:
                    pp1 += 1
                    print("Your score: ", pp1)
                else:
                    print("Better luck next time.... Correct workd is: ", chosen)
                    c= (int)(input("Press 1 to Continue or 0 to Quit"))

                    if c==0:
                        thank(p1name, p2name, pp1, pp2)
                        break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("1. Calculator\n"
          "2. Number Guess\n"
          "3. Jumbled Word Game")
    x= (int)(input("Select what operation you want to performm: "))


    if x==1:
        operations(4, 53, 25)

    elif x==2:
        print("Enter the range: ")
        lower = (int)(input("Enter lower bound-- "))
        upper = (int)(input("Enter upper bound-- "))
        numberGame(lower, upper)

    elif x==3:
        play()
