'''
https://adventofcode.com/2022/day/5
1.After the rearrangement procedure completes, what crate ends up on top of each stack?
2.After the rearrangement procedure completes, what crate ends up on top of each stack?

'''

def printStack(stos):
    for n, x in enumerate(stos):
        print(n+1, x)

columns = [[] for _ in range(9)]
with open(file='Day05/input.txt', mode='r') as file:
    i = 0
    for line in file:
        if line==' 1   2   3   4   5   6   7   8   9 \n':
            break
        for i in range(9):
            letter = line[1 + i * 4].strip()
            if letter:
                columns[i].append(letter)
    columns = [x[::-1] for x in columns]
    
    for line in file:
        if line=='\n':
            continue
        _, _many, _, _from, _, _to = line.strip().split(' ')
        for i in range(int(_many)):
            var = columns[int(_from)-1].pop()
            columns[int(_to)-1].append(var)

    for i in range(9):
        print(columns[i].pop(), end='')
    print(' \n')


columns = [[] for _ in range(9)]
with open(file='Day05/input.txt', mode='r') as file:
    i = 0
    for line in file:
        if line==' 1   2   3   4   5   6   7   8   9 \n':
            break
        for i in range(9):
            letter = line[1 + i * 4].strip()
            if letter:
                columns[i].append(letter)
    columns = [x[::-1] for x in columns]
    
    for line in file:
        if line=='\n':
            continue
        _, _many, _, _from, _, _to = line.strip().split(' ')
        temp = []
        for i in range(int(_many)):
            temp.append(columns[int(_from)-1].pop())
        for i in range(int(_many)):    
            columns[int(_to)-1].append(temp.pop())

    for i in range(9):
        print(columns[i].pop(), end='')
    print(' \n')