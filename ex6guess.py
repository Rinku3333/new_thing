import random
no = random.randint(0,100)
#print(no)
chance = 1
print("number of guesses is limited to 10 for both player ")

while (chance<=10):
    play1 = int(input("enter a integer guess here player1 : "))
    if play1  > no:

        print("your guess is more than the original no.")

    elif play1  < no:
        print("your guess is smaller than the original number")

    else:
        print("player 1 you won ")
        print(f"In {chance} chances u got it")
    play2= int(input("enter a integer guess here player2 : "))
    if play2  > no:

        print("your guess is more than the original no.")

    elif play2  < no:
        print("your guess is smaller than the original number")

    else:
        print("player 2 you won ")
        print(f"In {chance} chances u got it")
    chance=chance+1
if(chance > 10):
    print("game over buddy, no more chances remains")