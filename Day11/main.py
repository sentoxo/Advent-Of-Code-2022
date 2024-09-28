'''
https://adventofcode.com/2022/day/11
1. Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
2.Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?
'''
from pprint import pprint
monkeys = []
'''
0. [items list]
1. [op, x]    operation
2. x    test
3. x    iftrue
4. x    iffalse
5. x    inspection count
'''

'''
with open(file='Day11/input.txt', mode='r') as file:
    for i in range(8):
        _ = file.readline()
        items = file.readline().strip().split()
        operation = file.readline().strip().split()
        test = file.readline().strip().split()
        if_true = file.readline().strip().split()
        if_false = file.readline().strip().split()
        _ = file.readline()
        monkeys.append([[int(x.replace(',','')) for x in items[2:]], operation[4:], int(test[-1]), int(if_true[-1]), int(if_false[-1]), 0])

    for round in range(20):
        for monkey in monkeys:
            for obj in monkey[0]:
                if monkey[1][1] == 'old':
                    op = obj
                else:
                    op = int(monkey[1][1])
                if monkey[1][0] == '*':
                    obj *= op
                elif monkey[1][0] == '+':
                    obj += op
                obj = obj // 3
                if obj % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(obj)
                else:
                    monkeys[monkey[4]][0].append(obj)
                monkey[5]+=1
            monkey[0] = [] #empty items

    for monkey in monkeys:
        print(monkey[5])
    print('\n\n\n')

'''

with open(file='Day11/input.txt', mode='r') as file:
    for i in range(8):
        _ = file.readline()
        items = file.readline().strip().split()
        operation = file.readline().strip().split()
        test = file.readline().strip().split()
        if_true = file.readline().strip().split()
        if_false = file.readline().strip().split()
        _ = file.readline()
        monkeys.append([[int(x.replace(',','')) for x in items[2:]], operation[4:], int(test[-1]), int(if_true[-1]), int(if_false[-1]), 0])

    for round in range(10000):
        for monkey in monkeys:
            for obj in monkey[0]:
                if monkey[1][1] == 'old':
                    op = obj
                else:
                    op = int(monkey[1][1])
                if monkey[1][0] == '*':
                    obj *= op
                elif monkey[1][0] == '+':
                    obj += op
                obj = obj % 9699690 # *= monkeys[x].test
                if obj % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(obj)
                else:
                    monkeys[monkey[4]][0].append(obj)
                monkey[5]+=1
            monkey[0] = [] #empty items

    for monkey in monkeys:
        print(monkey[5])