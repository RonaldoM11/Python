print("Welcome to the Band Name Generator")
city1 = input("What's the name of the city your grew up in?\n")
name1 = input("What's your pets name?\n")
print("Your band name coud be ") 
print(city1, name1)

print("Hello World!\nHello World!\nHello World!" +  " " + "Ronnie")

input("What is your name?\n")
print("Hello " + input("what is your name?\n"))

# "# + /" comments out the whole line, "ctrl + z" undo

#       int takes in numbers
#        ^
num1 = int(input())
num2 = int(input())
print(num1 * num2)


#       str takes in words
#        ^
num1 = str(input())
num2 = str(input())
print(num1 + num2)

# len takes in the length or number of characters in a word.
#Example, Angela is a length of 6 characters.
#numOfLetters is the same as num1 or num2, its the place holder of what is being input by the user.
numOfLetters = len(input())
print(numOfLetters)
#The code below does the same thing as the code above. It is the simple version.
print(len(input()))


#python variables
#when asking a user for their name or input, the response given will be a data. We cannot use the data until it is given a name. 
#the example given, what is your name, user respondes with data, and we give it a variable "name".
#we then call name leter when printing and what gets printed is the data that was given a name. 
name = input("whats is your name?")
print(name)

print("\n")
print("example")
name = "jack"
print(name)
print("\n")
print("example")
name = "angela"
print(name)

print("\n")
#this example  does the same as the first set above, its asks the user for a name, and then the data is saved as variable "name".
#after the data is counted for the amount of characters within the variable, after it is then printed. 
name = input("what is your name?")
length = len(name)
print(length)



#more variables examples:
# THE INPUTS FOR THE EXAMPLE ARE 29 & 41
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇


#this is what i thought worked, which is a cheesy way of working but not the correct way.
#print("a: " + b)
#print("b: " + a)

#The correct way.
c = a
a = b 
b = c

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#naming variables can be simple
#example:
#name can be changed to "n" to be shorter, same for length as "l".
# n = input("what is your name?")
# l = len(n)
# print(l)

#1. Create a greeting for your program.
print("This program will generate your new band name!\n")
#2. Ask the user for the city that they grew up in.
city = input("what city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet = input("what is the name of your current pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your new band name is: " + city + " " + pet)
#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end