'''
https://adventofcode.com/2022/day/8
1.Consider your map; how many trees are visible from outside the grid?
2.Consider each tree on your map. What is the highest scenic score possible for any tree?
'''
test = """30373
25512
65332
33549
35390"""

matrix = []
with open(file='Day08/input.txt', mode='r') as file:
    for line in file:
        matrix.append([int(x) for x in line.strip()])
    
visible = set()

for i,row in enumerate(matrix):
    tallest = -1
    for j in range(0, len(row)):
        if row[j]>tallest:
            tallest=row[j]
            visible.add((i, j))
for i,row in enumerate(matrix):
    tallest = -1
    for j in range(len(row) - 1, -1, -1):
        if row[j]>tallest:
            tallest=row[j]
            visible.add((i, j))
for j in range(len(matrix[0])):  
    tallest = -1
    for i in range(len(matrix)):  
       if matrix[i][j] > tallest:
            tallest = matrix[i][j]
            visible.add((i, j))
for j in range(len(matrix[0])):  
    tallest = -1
    for i in range(len(matrix) - 1, -1, -1): 
        if matrix[i][j] > tallest:
            tallest = matrix[i][j]
            visible.add((i, j))
'''
for i in range(len(matrix[0])): #visualisation
    for j in range(len(matrix)):
        if (i, j) in visible:
            print(matrix[i][j],end='')
        else:
            print('-', end='')
    print()

print(len(visible)) #part1
'''

maxC = 0
for ii in range(len(matrix[0])): 
    for jj in range(len(matrix)):
        count = [0,0,0,0]
        tallest = matrix[ii][jj]
        for j in range(jj+1, len(matrix[0])):
            count[0]+=1
            if matrix[ii][j]>=tallest:
                break
        for j in range(jj-1, -1, -1):
            count[1]+=1
            if matrix[ii][j]>=tallest:
                break
        for i in range(ii-1, -1, -1):
            count[2]+=1
            if matrix[i][jj]>=tallest:
                break
        for i in range(ii+1, len(matrix)):
            count[3]+=1
            if matrix[i][jj]>=tallest:
                break
        maxC = max(count[0]*count[1]*count[2]*count[3], maxC)
print(maxC)
       