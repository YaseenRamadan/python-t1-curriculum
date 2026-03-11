import random # you must input random module to use 
num = random.randint(1,10) # generates a random number between 1 and 10 (inclusive)
guess = int(input("Guess a number between 1 and 10. "))
if guess == num:
    print("You guessed right! The number was", num)
else:
    print("You guessed wrong! The number was", num)