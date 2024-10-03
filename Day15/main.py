'''
https://adventofcode.com/2022/day/15
1.Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a beacon?
2.Find the only possible position for the distress beacon. What is its tuning frequency?
'''

ROW_Y = 2000000
not_here = set()
beacons_in_row = set()
with open(file='Day15/input.txt', mode='r') as file:
    for line in file: 
        line = line.strip().split()
        sx, sy = int(line[2][2:-1]), int(line[3][2:-1])
        bx, by = int(line[8][2:-1]), int(line[9][2:])
        distance = abs(sx-bx)+abs(sy-by)
        dist_from_row = abs(sy-ROW_Y)
        if dist_from_row <= distance:
            for i in range(sx - (distance-dist_from_row), sx + (distance-dist_from_row) +1):
                not_here.add( i )
        if by == ROW_Y:
            beacons_in_row.add(bx)
    result = len(not_here - beacons_in_row)
    print(result)



#part2

def is_outside_all_sensors(x, y, sensors):
    for sx, sy, distance in sensors:
        if (abs(sx-x)+abs(sy-y)) <= distance:
            return False
    return True

sensors = []
with open(file='Day15/input.txt', mode='r') as file:
    for line in file: 
        line = line.strip().split()
        sx, sy = int(line[2][2:-1]), int(line[3][2:-1])
        bx, by = int(line[8][2:-1]), int(line[9][2:])
        distance = abs(sx-bx)+abs(sy-by)
        sensors.append((sx,sy, distance))

    for sx, sy, distance in sensors:
        for dx in range(-distance-1, distance+2):
            dy = distance + 1 - abs(dx)
            foo = [(sx + dx, sy + dy), (sx + dx, sy - dy)]
            for x,y in foo:
                if 0 <= x <= 4000000 and 0 <= y <= 4000000 :
                    if is_outside_all_sensors(x, y, sensors):
                        print( x * 4000000 + y )
                        exit(0)