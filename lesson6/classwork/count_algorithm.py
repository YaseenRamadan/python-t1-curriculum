numbers = [14,1.50,3.2456,78, 0.0001]

counter = 0 #keep track of how many numbersso far in my list are greater than 5
for i in range(len(numbers)):
    if numbers[i] > 5: #check if the current number is greater than 5
        counter = counter + 1 #if it is greater than 5, add 1 to the counter
print("There are", counter, "numbers greater than 5 in the list.")

animals = ["cat", "dog", "rabbit", "hamster", "turtle", "cat", "cat", "dog", "hamster"]

counter2 = 0 #keep track of how many times we see "cat" in the list
for i in range(len(animals)):
    item = animals[i] #get the current item in the list
    if item == "cat": #check if the current item is "cat"
        counter2 = counter2 + 1 #if it is "cat", add 1 to the counter
print("There are", counter2, "cats in the list.")

num_cats = animals.count("cat")
print("There are", num_cats, "cats in the list.")  



