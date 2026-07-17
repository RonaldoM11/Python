#Day 9
#Dictionaries and Nesting

#DICTIONARIES
#This is a way to create a dictionary
#Example:
#{key : value}
#{"Bug" : "An error in a program that prevents the program from running as expected."}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from disctionary.
#print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#NESTING
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Struttgart"], 
}

#Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Struttgart"], "total_visits": 8}, 
}

#Nesting Dictionary in a List
travel_log = [
    {"country": "France", 
     "cities_visited": ["Paris", "Lille", "Dijon"], 
     "total_visits": 12
     },
    {"country": "Germany", 
     "cities_visited": ["Berlin", "Hamburg", "Struttgart"], 
     "total_visits": 8
     }, 
]


