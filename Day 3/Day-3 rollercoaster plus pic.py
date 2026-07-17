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




#using the "and" logical operator"
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
    elif age >= 45 and age <= 55:
       print("Everything is going to be ok. Have a free ride on us!")
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