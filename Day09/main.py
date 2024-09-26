'''
https://adventofcode.com/2022/day/9
1.Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
2.Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
'''


been = set()
cordX, cordY = 0, 0
cordXb, cordYb = 0, 0

def visualise(been):
    for i in range(17, -1, -1):
        for j in range(17):
            if (j, i) in been:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    print('')
        

with open(file='Day09/input.txt', mode='r') as file:

    for line in file:
        side, steps = line.strip().split(' ')
        steps = int(steps)

        for i in range(steps):
            #print((cordXb, cordYb))
            if side=='U':
                cordY+=1
                if abs(cordYb-cordY)>1 or abs(cordXb-cordX)>1:
                    cordYb = cordY-1
                    cordXb = cordX
                been.add((cordXb, cordYb))
            elif side=='D':
                cordY+=-1
                if abs(cordYb-cordY)>1 or abs(cordXb-cordX)>1:
                    cordYb = cordY+1
                    cordXb = cordX
                been.add((cordXb, cordYb))
            elif side=='R':
                cordX+=1
                if abs(cordYb-cordY)>1 or abs(cordXb-cordX)>1:
                    cordYb = cordY
                    cordXb = cordX-1
                been.add((cordXb, cordYb))
            elif side=='L':
                cordX+=-1
                if abs(cordYb-cordY)>1 or abs(cordXb-cordX)>1:
                    cordYb = cordY
                    cordXb = cordX+1
                been.add((cordXb, cordYb))
            #visualise(been)
            
    print('part 1', len(been))


#part2

def calculate(head, tail):
    h_x, h_y = head
    t_x, t_y = tail
    ret_x, ret_y = tail
    if abs(h_x-t_x)>1 or abs(h_y-t_y)>1:
        if h_x != t_x:
            ret_x += 1 if t_x<h_x else -1
        if h_y != t_y:
            ret_y += 1 if t_y<h_y else -1
    return (ret_x, ret_y)

been = set()
knots = [(0, 0) for _ in range(10)]
#been.add(knots[0])
with open(file='Day09/input.txt', mode='r') as file:

    for line in file:
        side, steps = line.strip().split(' ')
        steps = int(steps)

        for _ in range(steps):
            if side=='U':
                knots[0] = (knots[0][0], knots[0][1]+1)
            elif side=='D':
                knots[0] = (knots[0][0], knots[0][1]-1)
            elif side=='R':
                knots[0] = (knots[0][0]+1, knots[0][1])
            elif side=='L':
                knots[0] = (knots[0][0]-1, knots[0][1])

            for i in range(1, 10):
                knots[i] = calculate(knots[i-1], knots[i])

            been.add(knots[-1])
        #visualise(been)
            
    print('part 2', len(been))