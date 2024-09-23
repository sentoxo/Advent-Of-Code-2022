'''
https://adventofcode.com/2022/day/4
1. In how many assignment pairs does one range fully contain the other?
2. In how many assignment pairs do the ranges overlap?
'''


with open(file='Day04/input.txt', mode='r') as file:
    lines = file.readlines()
    count = 0
    countPart2 = 0 
    for line in lines:
        elf1, elf2 = line.strip().split(',')
        elf11, elf12 = (int(x) for x in elf1.split('-'))
        elf21, elf22 = (int(x) for x in elf2.split('-'))
        if (elf11 >= elf21 and elf12 <= elf22) or (elf21 >= elf11 and elf22 <= elf12):
            count+=1
        if (elf21 <= elf11 <= elf22) or (elf21 <= elf12 <= elf22) or (elf11 <= elf21 <= elf12) or (elf11 <= elf22 <= elf12):
            countPart2 += 1
    print(count, countPart2)
