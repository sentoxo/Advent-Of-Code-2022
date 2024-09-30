'''
https://adventofcode.com/2022/day/13
1.Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?
2.Organize all of the packets into the correct order. What is the decoder key for the distress signal?
'''

def compare(left, right) -> int:
    if isinstance(left, list) or isinstance(right, list):
        if not isinstance(left, list):
            left = [left]
        if not isinstance(right, list):
            right = [right]
        for i in range(max(len(left), len(right))):
            try:
                if (ret := compare(left[i], right[i])) != -1:
                    return ret
            except IndexError as _:
                if len(right) < len(left):
                    return 0
                if len(right) > len(left):
                    return 1
        return -1
    if left > right:
        return 0 #False
    elif left < right:
        return 1 #True
    else:
        return -1 #Continue

ans = 0
with open(file='Day13/input.txt', mode='r') as file:
    counter = 1
    for _ in range(150):
        line1 = eval(file.readline().strip())
        line2 = eval(file.readline().strip())
        _ = file.readline()
        ret = compare(line1, line2)
        if ret:
            ans += counter
        counter += 1
    print(ans)#part1


def compare3(left, right) -> int:
    ret = compare(left, right)
    if ret == 1:
        return -1
    elif ret == -1:
        return 0
    else:
        return 1

from functools import cmp_to_key
ans = 0
with open(file='Day13/input.txt', mode='r') as file:
    counter = 1
    foo = [[2], [6]]
    for _ in range(150):
        foo.append( eval(file.readline().strip()) )
        foo.append( eval(file.readline().strip()) )
        _ = file.readline()
    foo = sorted(foo, key=cmp_to_key(compare3))
    for i in range(len(foo)):
        if foo[i] in ([2], [6]):
            print(i+1)    #part2
    


        

