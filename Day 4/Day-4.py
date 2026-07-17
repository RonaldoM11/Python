#Day 4
#Randomisation and Python Lists


#Random Module

#commented out for reference
#import random
#import my_module

#random_integer = random.randint(1,10)
#print(random_integer)

#print(my_module.pi)

import random
randomInteger = random.randint(1, 10)
print(randomInteger)

#0.00000000 - 0.9999999....
randomFloat = random.random() * 5
print(randomFloat)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

#random_float * 5


#Heads or tails test
import random
random_side = random.randint(0,1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

#List:
#DATA STRUCTURE

#Example:
state1 = "Delaware"
state2 = "Pennsylvania"

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#                        0               1             2
#print(state_of_america[0]) <=== this prints Delaware, because of the order the data is saved in.
#if you use a negative index [-1] [-2] etc. , it starts counting the data backwards from the saved data.
# 
print(states_of_america)
print("Adding new rewritten state and appending ronnieland\n")
states_of_america[1] = "pencilvania"
# doing the above code will replace the previous saved data to the new data on thaty set index.
states_of_america.append("Ronnieland") 
#this gets aded to the end of the list
print(states_of_america)

#list.append(x)
#list.extend(iterable)
#list.insert(x)
#list.remove(x)
#list.pop(i)
#list.clear()
#list.index(x[, start[,end]])
#list.count(X)
#list.sort(*, key-note, reverse=false)
#list.reverse()
#list.copy()

#LESSON 14 DAY 4 - BANKER ROULETTE
# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
#names = names_string.split(", ")
# 🚨 Remember to remove the print statement above when you submit.
#import random
#num_items = len(names)
#random_choice = random.randint(0, num_items - 1)
#print(names[random_choice], "is going to buy the meal today!\n")



#state1 = "Delaware"
#state2 = "Pennsylvania"
#states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#num_of_states = len(states_of_america)
#print(states_of_america[num_of_states - 1])

#print(states_of_america[50])
#going past the data in the list, youll get an error like the line of code above. 


fruits = ["Strawberries", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Celery", "Tomatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)






#Coding challenge, really difficult.
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")



import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")