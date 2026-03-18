#A list is, apple bannana orange
#apple, banana, orange....
#1,2,3,4,5....
fruits = ["apple", "banana", "orange"]
#           0         1         2

y = len(fruits) #length is the same as length. The length of the fruits
print(y)

print(fruits)

print(fruits[0])
print(fruits[2])


vegtables = ["carrot", "broccoli", "spinach", "potato"]
#              0          1           2          3
c = len(vegtables)
print()




print(vegtables)
vegtables.append("mushroom") #APPEND adds to the end of the list
print(vegtables)

vegtables.insert(2,"carrot")
print(vegtables)

vegtables.remove("broccoli") #REMOVE removes the first instance of the item
print(vegtables)

vegtables.append("broccoli") #ADD adds to the end of the list
print(vegtables)
vegtables.append("broccoli")
print(vegtables)
vegtables.remove("broccoli")
print(vegtables)
c = vegtables.pop() #POP removes the item at the end and returns it
print(c)
print(vegtables)
b = vegtables.pop(2)
print(b)
print(vegtables)
m = vegtables.index("carrot") #INDEX returns the index of the first instance of the item
print(m)

vegtables.append("mushroom")
g = vegtables.count("mushroom") #COUNT counts how many times an item appears in the list
print(vegtables)
print(g)
