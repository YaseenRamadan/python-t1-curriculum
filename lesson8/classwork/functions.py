print("My name is Yaseen")

def make_greeting(): # define a function called make_greeting
    #name = input("What is your name? ")
    greeting = "Hello World!" #"Hello, " + name + "!"
    return greeting

message = make_greeting() # call the function
print(message)

# function that builds a face
def build_face():
    return ":)"

face = build_face()
print(face)
 
def print_poem():
    print("Roses are red,")
    print("Violets are blue,")
    print("Sugar is sweet,")
    print("And so are you.")

print_poem()
print_poem()

#Parameters are local variables that can only be acsessed within the function.
def pessonalized_greeting(name): #name is a parameter
    return "Hello, " + name + "!"

pesonalized_message = pessonalized_greeting("Yaseen") 
print(pesonalized_message)

# function that returns a rectangle area based on length and width
def rectangle_area(length, width): #length and width are parameters
    area= length * width
    return area

#When you call a function in a print statement, python will print what the function returns.
print("The area of a 5x3 rectangle is :", rectangle_area(5, 3))