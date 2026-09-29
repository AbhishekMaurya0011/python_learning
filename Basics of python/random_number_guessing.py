# WAP to create a random number guessing game and the input is given by the user.
import random
num=random.randint(1,15)
tries=0
while True:
    guess =int(input("Enter Number Which You Guess Between The 1 to 15: "))

    if guess>15:
        print(f"You Guess Invalid Number:{guess}")
        print("Please Enter Number Between 1 to 15")

    elif num==guess:
        print(f"You are Right and You Guess the Number in {tries} tries")
        tries+=1

    elif num<guess:
        print(f"You are Near Go a Little Lower of :{guess}")
        tries+=1

    else:
        print(f"You are Near Go a Little higher of :{guess}")
        tries+=1
    