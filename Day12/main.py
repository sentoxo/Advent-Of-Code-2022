'''
https://adventofcode.com/2022/day/12
1.What is the fewest steps required to move from your current position to the location that should get the best signal?

'''
'''part1
make w deque
add starting point
make a loop
  pop item
  check if we there
  loop for all4 directions
    check if we in boundires
      check if we werent there and eleveation <= 1
        add visited place to set
        add item to que with +1step
'''
'''
from collections import deque 
grid = []
with open(file='Day12/input.txt', mode='r') as file:
    for line in file:
        grid.append( [x for x in line.strip()] )
start = ()   
end = ()  
for i in range(len(grid)):
    try:
        id = grid[i].index('S')
        start = (i, id)
        grid[i][id] = 'a'
    except ValueError as _:
        pass
    try:
        id = grid[i].index('E')
        end = (i, id)
        grid[i][id] = 'z'
    except ValueError as _:
        pass

que = deque()
que.append((int(start[0]), int(start[1]), 0))
visited = set()
visited.add(start)

while que:
    y,x,s = que.popleft()

    if (y, x) == end:
        print(s)
        break

    for dx, dy in ( (0, 1), (0, -1), (1, 0), (-1, 0) ):

        nx = x+dx
        ny = y+dy

        if 0<=ny<len(grid) and 0<=nx<len(grid[0]):
            if (ny, nx) not in visited and ord(grid[y][x])-ord(grid[ny][nx])>-2:
                visited.add((ny, nx))
                que.append((ny,nx,s+1))
'''

def vis(grid, been):
    for y, row in enumerate(grid):
        for x, a in enumerate(row):
            if (y, x) in been:
                print('.', end='')
            else:
                print(a, end='')
        print('')

#vis(grid, visited)

from collections import deque 
grid = []
with open(file='Day12/input.txt', mode='r') as file:
    for line in file:
        grid.append( [x for x in line.strip()] )
start = ()   
for i in range(len(grid)):
    try:
        id = grid[i].index('E')
        start = (i, id)
        grid[i][id] = 'z'
    except ValueError as _:
        pass

que = deque()
que.append((int(start[0]), int(start[1]), 0))
visited = set()
visited.add(start)

while que:
    y,x,s = que.popleft()

    if grid[y][x] == 'a':
        print(s)
        break

    for dx, dy in ( (0, 1), (0, -1), (1, 0), (-1, 0) ):

        nx = x+dx
        ny = y+dy

        if 0<=ny<len(grid) and 0<=nx<len(grid[0]):
            if (ny, nx) not in visited and ord(grid[y][x])-ord(grid[ny][nx])<2:
                visited.add((ny, nx))
                que.append((ny,nx,s+1))