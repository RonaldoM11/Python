with open("file1.txt") as file1:
    file1_numbers = [int(line.strip()) for line in file1]

with open("file2.txt") as file2:
    file2_numbers = [int(line.strip()) for line in file2]

result = [num for num in file1_numbers if num in file2_numbers]

print(result)

#"file1.txt"
#1
#2
#3

#"file2.txt"
#2
#3
#4

#Output will be [2, 3]