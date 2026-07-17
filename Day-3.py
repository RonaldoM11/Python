#Day 3:
#Conditional Statements, Logical Opertators, Code Blocks and Scopes

#Conditional: 
# if / else statements
# if condition:
#   do this
# else:
#    do this

#example:
#water_level = 50
#if water_level > 80:
#    print("DrainWater")
#else:
#    print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("Whats is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride!")

#Comparson Operators:
#   >   greater than
#   <   less than
#   >=  greater than or equal to
#   <=  less than or equal to
#   ==  equal to
#   !=  not equal to

#Lesson 8 Day 3 - ODD or EVEN
#this code tests the users input of a number and determines if it is odd or even. 

# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆
print(number)
# Write your code below this line 👇
if (number % 2) == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#Nested if / else statements
#if condition:
#    if another condition:
#        do this
#    else:
#        do this
# else:
#  do this

#Example:
#This is an example with only one conditional.
print("Welcome to the rollercoaster!")
height = int(input("Whats is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
       print("Please pay $7.00")
    else:
       print("Please pay $12.00")
else:
    print("Sorry, you have to grow taller before you can ride!")

#Example:
#This is an example with more than one conditional - if/elif/else statements
#You can add as many elif's as you want to make the conditions in your 
# code to work that way you expect them to work

#if condition1:
#   do A
#elif condition2:
#   do B
#else:
#   do this

print("Welcome to the rollercoaster!")
height = int(input("Whats is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
       print("Please pay $5.00")
    elif age <= 18:
       print("Please pay $7.00")
    else:
       print("Please pay $12.00")
else:
    print("Sorry, you have to grow taller before you can ride!")


#LESSON 9 DAY 3 - BMI 2.0
# Write your code below this line 👇
height = float(input())
weight = int(input())
#bmi = new_weight / new_height ** 2
bmi = weight / (height * height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
   print(f"Your BMI is {bmi}, you are clinically obese.")


#LESSON 10 DAY 3 - LEAP YEAR
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else: 
      print("Not leap year")
  else: 
    print("Leap year")
else:
  print("Not leap year")


print("Welcome to the rollercoaster!")
height = int(input("Whats is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
       bill = 5
       print("Child tickets are $5.00")    
    elif age <= 18:
       bill = 7
       print("Youth tickets are $7.00")
    else:
       bill = 12
       print("Adult tickets are $12.00")
    pic = input("Would you like a photo taken? Y or N. ")
    if pic == "Y":
        bill = bill + 3
        #bill += 3 does the same as above.
    print(f"That will be an extra $3.00. Your total will be ${bill}.00") 
else:
    print("Sorry, you have to grow taller before you can ride!")


#PIZZA ORDER PRACTICE
print("Thank you for choosing Python Pizza Deliveries!")
size = input("what size pizza do you want? S, M, L ? ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N? ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N? ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
  
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${bill}.")



#LOGICAL OPERATORS
#   and 
#   or    
#   not 



#love calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")