'''
https://adventofcode.com/2022/day/10
1.Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
2.Render the image given by your program. What eight capital letters appear on your CRT?
'''

with open(file='Day10/input.txt', mode='r') as file:

    x = 1
    cycles = 0
    ans = 0
    for line in file:
        command = line.strip().split()
        d = 0
        c = 1
        if command[0] == 'addx':
            d = int(command[1])
            c+=1
            
        for i in range(c):
            cycles += 1
            if cycles in (20, 60, 100, 140, 180, 220):
                ans += cycles*x
            
            if i==1:
                x += d
    print(ans)


with open(file='Day10/input.txt', mode='r') as file:

    x = 1
    vga = []
    cycles=-1
    for line in file:
        command = line.strip().split()
        d = 0
        c = 1
        if command[0] == 'addx':
            d = int(command[1])
            c+=1
            
        for i in range(c):
            #print(cycles, x)
            cycles += 1

            if abs(cycles%40-x)<2:
                vga.append('#')
            else:
                vga.append('.')
            if i==1:
                x += d

    for x in range(len(vga)//40):
        for y in range(40):
            print(vga[y+x*40], end='')
        print()