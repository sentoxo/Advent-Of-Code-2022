'''
https://adventofcode.com/2022/day/1
1. Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
2. Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
'''

arr = []
sum = 0

with open(file='Day01/input.txt', mode='r') as file:
    for line in file:
        try:
            sum += int(line)
        except ValueError as _:
            arr.append(sum)
            sum = 0
    print(max(arr)) #part1


    sum = 0
    arr.sort(reverse=True)
    for i in range(3):
        sum += arr[i]
    print(sum) #part2