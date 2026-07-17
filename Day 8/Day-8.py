#Day-8
#Functions with Inputs

#Simple Function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isnt't the weather nice today?\n")

greet()

#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")
    print(f"Isn't the wather nice today?\n")

greet_with_name("Ronnie")


#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?\n")
greet_with("Ronnie", "France")

#Functions with keyword arguments
def greet_with(name="Ronnie", location="France"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with()


