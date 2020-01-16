import random

correctGuess = random.randint(1,20)
print(correctGuess)

numberGuesses=0
while numberGuesses < 6:
    guess = input("Take a guess")
    try:
        guess = int(guess)
        numberGuesses = numberGuesses + 1
        if guess == correctGuess:
            print("Good job! Guessed correctly in %d guesses" % numberGuesses)
            break
        elif guess > correctGuess:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
    except ValueError:
        print("Please enter only numbers")




if numberGuesses == 6:
    print("The correct number is "+str(correctGuess))