pet = "cat"

def show_pet():
    print("the pet is", pet)

show_pet() 

#error: changing global variable without declaring 'global'
# def adopt_dog():
#     print("the old pet is", pet)
#     pet = "dog"
# adopt_dog()
# show_pet()

def adopt_parrot():
    global pet
    pet = "parrot"

adopt_parrot()
show_pet()