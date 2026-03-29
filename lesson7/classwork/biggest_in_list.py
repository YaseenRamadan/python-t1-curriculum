numbers = [5, -8, 35, 13, 6, 2]
print (numbers)

# You can use the built in python function to find the biggest number in a list
biggest = max(numbers)
smallest = min(numbers)
print("The biggest number is:", biggest)
print("The smallest number is:", smallest)

print("Our algorithm:")

biggest2 = numbers[0] #Start by assuming the first number is the biggest
for i in range (len(numbers)): #Go through each index in the list
    if numbers[i] > biggest2: #If the item is bigger than our current biggest number
        biggest2 = numbers[i] #Update our biggest number to be the item

print("The biggest number is:", biggest2)
