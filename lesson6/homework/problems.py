# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print(names.count("Alex"))



# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
if "elephant" in animals:
    print("Elephant found!")
else:
    print("Elephant not found.")

# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print(scores.count(100))

counter = 0
for i in range(len(scores)):
    if scores[i] == 100:
        counter = counter + 1
print(counter)
# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
index = -1
if "blue" in colors:
    index = colors.index("blue")
print(index)

index = -1
for i in range(len(colors)):
    if colors[i] == "blue":
        index = i
        break
print(index)
# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
counter = 0
for i in range(len(temperatures)):
    if temperatures[i] < 0:
        counter = counter + 1
print(counter)