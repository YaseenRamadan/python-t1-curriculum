# Problem 1
# Write a function that returns the number 42 and print the result.
def return_42():
    return 42
print(return_42())
# Problem 2
# Write a function that returns "penguin" and print the result.
def return_penguin():
    return "penguin"
print(return_penguin())
# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.
fruit = "apple"
print(fruit)
def change_fruits():
    global fruit
    fruit = "banana"
change_fruits()
print(fruit)

# Problem 4
# Write a function that takes two parameters: first_name and last_name.
# The function should return a string that combines the first and last names separated by a space.
def combine_names(first_name, last_name):
    return first_name + " " + last_name
print(combine_names("Luke", "Ismael"))
# Problem 5
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).
def calculate_perimeter(length, width):
    return 2 * (length + width)
print(calculate_perimeter(5, 3))