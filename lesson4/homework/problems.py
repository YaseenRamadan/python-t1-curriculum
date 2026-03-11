# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
testscore1 = int(input("What is your test score?"))
testscore2 = int(input("What is your test score?"))
if testscore1 >= 50 and testscore2 >= 50:
    print("You passed both!")
else:
    print("You failed at least one.")

# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch = input("Did you bring lunch? yes/ no")
water = input("Did you bring water? yes/ no")
if lunch == "yes" or water == "yes":
    print("You're somewhat ready.") 

if lunch == "yes" and water == "yes":
    print("You're fully ready.")

if lunch == "no" and water == "no":
    print("You're not ready.")

# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
number = int(input("Enter a number."))
if number > 10:
    print("Out of range.")
else:
    print("In range.")

# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
num = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10. "))
if num == guess and guess % 2 == 0:
    print("Even match!")
elif num == guess or num == 5:
    print("Nice try!")
else:
    print("Nope.")

# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."

number1 = int(input("Enter a number."))
number2 = int(input("Enter a number."))
if number1 % 5 == 0 and number2 % 2 != 0:
    print("Interesting pair!") 
else:
    print("Plain pair.")