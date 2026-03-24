# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
day = input("Enter the day of the week (all lowercase): ")
if day == "saturday" or day == "sunday":
    print("Weekend")
else:
    print("Weekday")



# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
import random
num = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == num:
    print("Correct!")
else:
    print("Try again!")

# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
int = int(input("Enter a positive ineger:"))
if int > 10 and int % 2 == 0:
    print ("Big even number")
else:
    print ("number does not meet criteria")

# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num1, "is larger than", num2)
elif num2 > num1:
    print(num2, "is larger than", num1) 
else:
    print("Numbers are equal.")