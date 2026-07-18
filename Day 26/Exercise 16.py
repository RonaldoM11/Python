list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers =  list(map(int, list_of_strings))
result = [num for num in numbers if num % 2 == 0]
print(result)

#Output needs to be [0, 32, 8, 2, 8, 64, 42]