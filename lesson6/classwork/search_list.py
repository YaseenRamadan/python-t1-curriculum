fruits = ["apple", "banana", "orange"]

# Find if apple is in the list
if "apple" in fruits:
    print("found apple.")
else:
    print("apple not found.")

# Algorithm is a step by step problem (solving process).
found = False
index = -1
for i in range(len(fruits)): #looping through the list using the index
    if fruits[i] == "apple":
        found = True # Mark as found
        index = i # Store the index where apple is found
        break #Exit the loop since we found apple
if found == True:
    print("found apple at index", index)
else:
    print("no apples in list.")
