'''
https://adventofcode.com/2022/day/7
1.Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
2.Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

'''
import pprint

with open(file='Day07/input.txt', mode='r') as file:
    dicti = dict()
    directory = []
    for line in file:
        match line.strip().split(' '):
            case '$', '/': directory = []
            case '$', 'cd', '..': directory.pop()
            case '$', 'cd', x: directory.append(x+'/')
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for i in range(len(directory) + 1):
                    temp_dir = ''.join(directory[:i])
                    dicti[temp_dir] = dicti.get(temp_dir, 0) + int(size)
    
    pprint.pprint(dicti)
    print(sum( (x for x in dicti.values() if x<=100_000) ))
    print(min( (x for x in dicti.values() if x >= dicti['//']-40_000_000) ))