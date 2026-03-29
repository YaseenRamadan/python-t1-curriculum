numbers = [5, -8, 35, 13, 6, 2]

total = sum(numbers) #Shortcut to find the sum
print("The sum is:", total)

print("Our algorithm:")
total2 = 0
for i in range(len(numbers)): #Go through each index in the list
    item = numbers[i] #Get the item at the current index
    total2 = total2 + item #Add the item to the total
print("The sum is:", total2)

# Find the sum of only positive numbers

total3 = 0
for i in range(len(numbers)): #Go through each index in the list
    item = numbers[i]
    if item > 0: #Only add the item if it is positive
        total3 = total3 + item
print("The sum of positive numbers is:", total3)