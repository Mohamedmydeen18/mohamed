import random
number=random.randint(1,10)
guess=0
while guess!=number:
    guess = int(input("Enter Guess:"))
    if (guess<number):
        print("Guess higher!")
    elif(guess>number):
        print("Guess number")
    else:
        print("YOU WON !")        
        