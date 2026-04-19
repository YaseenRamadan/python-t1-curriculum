# Problem 1
# Use a while loop to print the word "Python" 4 times.
i = 1
while i <= 4:
    print("Python")
    i = i + 1

# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).
i = 2
while i <=12:
    print(i)
    i = i + 2

# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.
num = int(input("Enter a positive number:"))
i = 0
while i <= num:
    print (i)
    i = i + 1

# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.
num = int(input("Enter a starting number greater than 10:"))
while num >= 0:
    print(num)
    num = num - 5

# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
animals = ["dog", "cat", "fish"]
i = 0
while i < len(animals):
    print(animals[i] + " is awesome!")
    i = i + 1