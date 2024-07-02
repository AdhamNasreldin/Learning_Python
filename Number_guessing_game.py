import random

print(" Welcome in our guessing game , you have 6 trials to get a number between 1 and 100")
x = random.randint(1,100)
y = int(input("guess a number "))
z = False
for i in range(1,7):
    if (y == x ):
        print("correct")
        z = True
        break
    elif (i==6) :
        print("You lost the game , the number was " + str(x))
        break
    elif (y > x) :
        y= int(input ("too high , guess again "))
    elif (y< x) :
         y=int (input ("too low , guess again "))
    print( str(5-i)+" guesses left ")
