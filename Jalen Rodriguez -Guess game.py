# A guess game program made in python
import random

guessesTaken = 0

print('Hello! What is your name')
myName = input()

number = random.randint(1, 50)
print('Well, {}, I am thinking of a number between 1 and 50'.format(myName))

while guessesTaken < 5:
    print('Take a guess..')
    guess = input()
    guess = int(guess)

    guessesTaken += 1

    # Instead of calling the variable itself then adding 1

    if guess < number:
        print('Your number guess is too low, guess again')

    if guess > number:
        print('Your number is too high! guess lower or something!')

    if guess == number:
        print('Good job, {}! You guessed the right number in {} guesses!'.format(myName, guessesTaken))
        break
