# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
total = 0
for i in range(len(numbers)):
    if numbers[i] > 25:
        total += numbers[i]
print(total)

# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
numbers = [-5, -20, -11, 0, 4, -15]
total = 0
for i in range(len(numbers)):
    if numbers [i] < -10:
        total += numbers[i]
print(total)

# Problem 3
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]
biggest = -float('inf')
for i in range(len(numbers)):
    if numbers [i] < 100:
        biggest = max(biggest, numbers[i])
    print("...", biggest)
print(biggest)

# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
biggest = -float('inf')
for i in range(len(numbers)):
    biggest = max(biggest, numbers[i])
print(biggest)

# Problem 5
# Find and print the total sum of all the numbers in the list.
numbers = [1, 3, 5, 7, 9]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
print(total)