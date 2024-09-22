'''
https://adventofcode.com/2022/day/2
1. What would your total score be if everything goes exactly according to your strategy guide?
2. Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

A   Rock        X   Lose
B   Paper       Y   Draw
C   Scissors    Z   Win


'''

points = 0

with open(file='Day02/input.txt', mode='r') as file:
    for line in file:
        him, me = line.strip().split(' ')
        if me == 'X':
            points += 1
            if him == 'A':
                points += 3
            elif him == 'B':
                points += 0
            elif him == 'C':
                points += 6
        elif me == 'Y':
            points += 2
            if him == 'A':
                points += 6
            elif him == 'B':
                points += 3
            elif him == 'C':
                points += 0
        elif me == 'Z':
            points += 3
            if him == 'A':
                points += 0
            elif him == 'B':
                points += 6
            elif him == 'C':
                points += 3
    print(points) #part1
        
    
points = 0

with open(file='Day02/input.txt', mode='r') as file:
    for line in file:
        him, me = line.strip().split(' ')
        if me == 'X':
            points += 0
            if him == 'A':
                points += 3
            elif him == 'B':
                points += 1
            elif him == 'C':
                points += 2
        elif me == 'Y':
            points += 3
            if him == 'A':
                points += 1
            elif him == 'B':
                points += 2
            elif him == 'C':
                points += 3
        elif me == 'Z':
            points += 6
            if him == 'A':
                points += 2
            elif him == 'B':
                points += 3
            elif him == 'C':
                points += 1
    print(points) #part2
        