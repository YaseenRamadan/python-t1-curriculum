# Problem 1
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]
total = sum(numbers) 
print("The sum is:", total)

# Problem 2
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0]
biggest = max(numbers)
print( "The biggestnumber is:", biggest)


# Problem 3
# Find and print the sum of only the negative numbers in the list (negative means less than 0).
numbers = [2, -1, 8, 10, -7, 6]
total = sum(x for x in numbers if x < 0)
print("The sum of negative numbers is:", total)

print("Our algorithm:")
total2 = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item < 0:
        total2 = total2 + item
print("The sum of negative numbers is:", total2)

# Problem 4
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]
total = sum(x for x in numbers if x % 2 == 0)
print("The sum of even numbers is:", total)

print("Our algorithm:")
total2 = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item % 2 == 0:
        total2 = total2 + item
print("The sum of even numbers is:", total2)
# Problem 5
# Find and print the biggest number that is negative in the list.
numbers = [-1, -30, -5, 7, 12, -2]
biggest_negative = -9999
for i in range (Len(numbers)):
    if numbers[i] < 0 and numbers[i] > biggest_negative:
        biggest_negative = numbers[i]

