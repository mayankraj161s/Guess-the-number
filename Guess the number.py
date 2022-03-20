# Game : Guess the number in a limited number of attempts.
print("\nWelcome to the game : GUESS THE NUMBER")
print("-"*38)
def guess():
    print("RULES:")
    print("-"*6)
    print("1) Total no. of attempts = 9")
    import random
    num = random.randint(0, 50)
    a = 9
    for i in range(9):
        num1 = int(input("---->Guess the number: "))
        if num1 != num:
            print("You have",a-1,"attempts left.")
            a -= 1
        elif num1 == num:
            print("You won!!!")
            highest = 'You guessed the the right number in '+str(i+1)+' attempts.'
            print(highest)
            break
        if a == 0:
            print("Game Over.")
            print("You Lost.")
            break
        if num1 < num:
            print("You guessed a lower number.")
            print("Try higher.")
        if num1 > num:
            print("You guessed a higher number.")
            print("Try lower.")
    print("-"*70)
name = input("Enter your name to start:")
while True:
    if name.isalpha():
        print("Hello,",name,"Now start playing.")
        guess()
        break
    else:
        print("Incorrect name.")
        name = input("Enter your name again:")
