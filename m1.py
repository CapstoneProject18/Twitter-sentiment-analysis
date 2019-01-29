''''
pseudocode
-------------------------------------
#1 import random module
#2 input name
#3 while loop:
    if > number      //higher
    elif < number   // lesser
    elif == number //  equal
    
'''
import random
guessesTaken = 0
myName = input('Hey there! What is your name?')
number = random.randint(1, 20)

print('Whassup, ' + myName + ', I am thinking of a number between 1 and 20.')
while guessesTaken < 10:
     print('Take a guess.')
     guess = input()
     guess = int(guess)

     guessesTaken = guessesTaken + 1

     if guess < number:
         print('Your guess is too low. Attempts = ' + str(guessesTaken))

     elif guess > number:
         print('Your guess is too high. Attempts = ' + str(guessesTaken))

     elif guess == number:
         break

     else:
        print("Error. Please type a valid input.")


if guess == number:
     guessesTaken = str(guessesTaken)
     print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

elif guess != number:
     number = str(number)
     print('Sorry.  You exceeded the maximum number of guesses. The number I was thinking of was ' + number)


