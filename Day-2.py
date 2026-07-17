#primitive data types
#data types: strings, integers, Floats, Booleans

#Strings:
#pulling the first character of a string is called "subscripting"
#first character of "hello" is polace holder 0
print("Hello"[0])
# place holder 0 will print out "H"

print("Hello"[4])
# 4 place holder will print out "o"

#Interger:
print("123" + "345")
#prints "123345", it just puts both together, or its being concatenating. 
# CONCATENATING: link (things) together in a chain or series.

print(123 + 345)
#this example literally does the math 123 + 345.
#prints "468"

#Float:
#floating point number
#3.14159


#Boolean:
#Two possible values, True or False.


#Example:
# num_char = len(input("What is your name?"))
#the code below is what most beginners would do to try and display the amount of characters in the data.
# print("Your name has " + num_char + " characters.")
# print(type(num_char))

#type conversion/ type casting
# new_num_char = str(num_char)

#The way the beginners work could work is by creating a new place holder for the old. 

num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

#a = str(123)
# "a" can be either a string, float, or integer becuase that is the data type that we can convert it to.
#print(type(a))


print(70 + float("100.5"))
print(str(70) + str(100))



#My Test of getting a two digit number and adding first digit + second digit
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
first_single_number = int(two_digit_number[0])
second_single_number = int(two_digit_number[1])
print(first_single_number + second_single_number)

#Instructors Version.
two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)


#My test for BMI problem
# 1st input: enter height in meters e.g: 1.65
#height = input()
# 2nd input: enter weight in kilograms e.g: 72
#weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
#new_weight = str(weight)
#new_height = float(height)
#bmi = (new_weight / (new_height ** 2))
#print("BMI is: " + bmi)

#The correct way
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
new_weight = int(weight)
new_height = float(height)
#bmi = new_weight / new_height ** 2
bmi = new_weight / (new_height * new_height)
new_bmi = int(bmi)
print("The BMI is: \n")
print(new_bmi)
print("THE BMI is: " + str(new_bmi))
print("\n")
#Example of using *, -, +, / for with a new output of the previous output.
#score = 2 <----------------------------
#                                      |
#score *= 2 will be previous score of "2" * new score of 2 = 4, new_score = 4
#         ^----------------------------------------------|
#print(score) = "4"

#score -= 2, = 0
#score += 2, = 4
#score /= 2, = 1



#f-string:
#f strings cut down on having to use "+" when using print statements.
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
print("\n")


#This example tests a users age and will give the remaining amount of weeks left until they are 90.
print("whats is your age?")
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} weeks left.")


#Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
#total = int(tip) / 100 * bill + bill
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

