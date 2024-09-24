'''
https://adventofcode.com/2022/day/6
1.How many characters need to be processed before the first start-of-packet marker is detected?

'''


with open(file='Day06/input.txt', mode='r') as file:
    line = file.readline()
    
    i = 0
    while True:
        s = set()
        s.add( line[i] )
        s.add( line[i+1] )
        s.add( line[i+2 ])
        s.add( line[i+3] )
        if len(s)==4:
            print(i+4)
            break
        i+=1
    

with open(file='Day06/input.txt', mode='r') as file:
    line = file.readline()
    
    i = 0
    while True:
        s = set()
        for n in range(14):
            s.add( line[i+n] )
        if len(s)==14:
            print(i+14)
            break
        i+=1 # You can move faster if you check how many character can be omitted
    