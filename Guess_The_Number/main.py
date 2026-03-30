import random

sortedNumber = random.randint(1,100)
guess = 0
print("")
print("<<< GUESS GAME >>>")
print("")

while sortedNumber != guess:
    guess = int(input("Guess a number between 0 and 100: "))

    if guess < sortedNumber:
        print("Your number is BELOW the number sorted - try again")
        print("")

    elif guess > sortedNumber:
        print("Your number is ABOVE the number sorted - try again")
        print("")

    else:
        print("CONGRATULATIONS! You found, the secret number is " + str(sortedNumber))




