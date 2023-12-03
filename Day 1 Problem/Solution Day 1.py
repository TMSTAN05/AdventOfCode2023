#import input file from AoC
with open('/workspaces/AdventOfCode2023/Day 1 Problem/Code Advent Day 1.csv', 'r') as file:
    dataset_lines = file.readlines()

#Remove trailing newlines or spaces
dataset_lines = [line.strip() for line in dataset_lines]

#initialize problem sums
problem_1 = 0
problem_2 = 0

#Iterate through each line in the dataset
for line in dataset_lines:
    #Lists to store digits found in the current line
    problem_1_digits = []
    problem_2_digits = []

    #Enumerate through each character in the line
    for i, c in enumerate(line):

        #If the character is a digit, add it to both lists
        if c.isdigit():
            problem_1_digits.append(c)
            problem_2_digits.append(c)

        #Check for spelled out numbers in the line    
        for d, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            #If a spelled out number is found, add its corresponding digit to the p2 list
            if line[i:].startswith(value):
                problem_2_digits.append(str(d+1))

    #Add the two digit number formed by the first and last digits to the part 1 sum
    problem_1 += int(problem_1_digits[0] + problem_1_digits[-1])

    #Add the two digit number formed by the first and last digits (including spelled out) to the part 2 sum
    problem_2 += int(problem_2_digits[0] + problem_2_digits[-1])

#print results
print(f'Problem 1: {problem_1}', f'\n Problem 2: {problem_2}') 