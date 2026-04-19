# Problem 1
# Use a while loop to print the numbers from 1 to 7 (inclusive).
i = 1
while i <= 7:
    print(i)
    i = i + 1

# Problem 2
# Use a while loop to count down from 3 to -3 (inclusive), printing each number.
i = 3
while i >= -3:
    print(i)
    i = i - 1


# Problem 3
# Ask the user to input a number less than 50.
# Use a while loop to print numbers starting from that number, going up by 2 each time, until you reach 50 (inclusive).
user = int(input("Enter a number less than 50:"))
i =user
while i <+50:
    print(i)
    i = i + 2
# Problem 4
# Ask the user to input a number.
# Use a while loop to count down by 3 each time until you reach 0 or less (inclusive).
user = int(input("Enter a number:"))
i = user
while i >= 0:
    print(i)
    i = i - 3

# Problem 5
# Use a while loop to print each element in the list.
items = ["chair", "table", "desk"]
i = 0
while i < len(items):
    print(items[i])
    i = i + 1




#Print numbers from 1 to 5 using a while loop.
i = 1
while i <= 5:
    print(i)
    i = i + 1
#Print numbers from 5 down to 1 using a while loop.
i = 5
while i >= 1:
    print(i)
    i = i - 1
#Print all multiples of 3 from 3 up to 30 using a while loop.
i = 3
while i <= 30:
    print(i)
    i = i +3
#Use a while loop to find the sum of the numbers 1 through 5.
i = 1
sum = 0
while i <= 5:
    sum = sum + i
    i = i + 1
print(sum)
#Ask the user for a number N, then print all numbers from N down to 1 using a while loop.
N = int(input("Enter a number:"))
i = N
while i >= 1:
    print(i)
    i = i - 1
#Given a number like 456, print each digit on a new line using a while loop (starting from the last digit).
number=456
digit = 0
while number > 0:
    digit = number % 10
    print(digit)
    number = number // 10

#Given a number like 456, use a while loop to find the sum of its digits.
number = 456
sum = 0
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
print(sum)

#Keep asking the user to enter the number 7. Only stop when they finally enter 7
while True
    user = int(input("Enter the number 7:"))
    if user == 7:
        break




factorial:

result = 1
num = 3
for i in range(num):
    result = num * result
    num = num - 1
    if num == 0:
        break
print(result)