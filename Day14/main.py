'''
https://adventofcode.com/2022/day/14
1.Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?
2.Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?
'''
def visualise(been):
    for i in range(0,180):
        print(i, end='')
        for j in range(450,580):
            if (j, i) in been:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    print('')

grid = set() # (y,x)
with open(file='Day14/input.txt', mode='r') as file:
    for line in file:
        prev = None
        line_splited = line.strip().split(" -> ")
        for t in line_splited:
            y,x = (int(x) for x in t.split(','))
            if prev:
                prev_y, prev_x = prev
                if prev_y == y:
                    if x > prev_x:
                        for i in range(prev_x, x+1):
                            grid.add((y,i))
                    else:
                        for i in range(x, prev_x+1):
                            grid.add((y,i))
                elif prev_x == x:
                    if y > prev_y:
                        for i in range(prev_y, y+1):
                            grid.add((i,x))
                    else:
                        for i in range(y, prev_y+1):
                            grid.add((i,x))
                prev = (y,x)
            else:
                prev = (y,x)

    for i in range(0,1000):
        grid.add((i, 176))

    #PART 2
    counter = 0
    ON = True
    while(ON):
        y,x = 500, 0
        while(True):
            if (y, x+1) not in grid:
                x+=1
                continue
            if (y-1, x+1) not in grid:
                y-=1
                x+=1
                continue
            if (y+1, x+1) not in grid:
                y+=1
                x+=1
                continue
            if x==0:
                ON = False
                break
            counter+=1
            grid.add((y,x))
            break
    
    print(counter)
    visualise(grid)

'''PART1
    counter = 0
    ON = True
    while(ON):
        y,x = 500, 0
        while(True):
            if x>180:
                ON = False
                break
            if (y, x+1) not in grid:
                x+=1
                continue
            if (y-1, x+1) not in grid:
                y-=1
                x+=1
                continue
            if (y+1, x+1) not in grid:
                y+=1
                x+=1
                continue
            counter+=1
            grid.add((y,x))
            break
    
    print(counter)
    visualise(grid)
    '''