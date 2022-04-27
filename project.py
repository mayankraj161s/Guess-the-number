import datetime
import os
import random
def guess():
    low = 1 ; high = 50
    print("Total Attempts = 7")
    n = random.randint(1,50)
    for i in range(1,8):
        num = int(input("Guess the number b\w {} and {}: ".format(low,high)))
        if num == n:
            return i
        elif i == 7:
            return 0
        elif num > 50 or num < 0:
            return 100
        elif num > n:
            print("Try lower.")
            high = num
        elif num < n:
            print("Try higher.")
            low = num
print("***********************************")
print("WELCOME TO THE GAME : GUESS THE NUMBER")
print("***********************************")
name = input("Enter your Name : ")
print("\nHello {}, Now start playing".format(name))
game = guess()
if game != (0 and 100):
    print("\nYou guessed it right in",game,"attempts.")
elif game == 0:
    print("\nGame Over!")
    print("You ran out of attempts.")
elif game == 100:
    print("Out of Range")
    print("Game Over")

# Changing Directory to Directory Containing this project.py
try:
    os.mkdir("Persons")              # Creating person directory
except FileExistsError:
    pass

# Writing onto text file
my_file = open("Persons\{}.txt".format(name),'a+')
my_file.seek(0)
if my_file.read(4) != "NAME":
    my_file.write("NAME : {}".format(name.upper()))
my_file.write("\n*****************************\n\n")
my_file.write(str(datetime.datetime.now()))
if game != 0 and 100:
    my_file.write("\nAttemps Taken: {}\n\n".format(game))
else:
    my_file.write("\nYou didn't guess the right number.\n\n")