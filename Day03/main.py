'''
https://adventofcode.com/2022/day/3
1. Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
2. Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
'''

pioritySum = 0
lineN = 0
thereis = 0
with open(file='Day03/input.txt', mode='r') as file:
    for line in file:
        arr1 = [0]*128
        arr2 = [0]*128
        lineN += 1
        text = line.strip()
        compartment1 = text[:len(text)//2]
        campartment2 = text[len(text)//2:]
        for x in compartment1:
            arr1[ord(x)] = 1
            #print(ord(x), end=" ")
        #print('')
        for x in campartment2:
            arr2[ord(x)] = 1
            #print(ord(x), end=" ")
        #print('')
        check = False
        for i in range(128):
            if arr1[i]==1 and arr2[i]==1:
                check = True
                #print(compartment1, campartment2, i)
                thereis += 1
                if ord('A') <= i <= ord('Z'):
                    pioritySum += (i - ord('A') + 27)
                    #print(chr(i), (i - ord('A') + 27))
                else:
                    pioritySum += (i - ord('a') + 1)  
                    #print(chr(i), (i - ord('a') + 1))
        #if check==False:
            #print(compartment1, campartment2, i)
    print('->', pioritySum)
    #print(lineN, thereis)


pioritySum = 0

with open(file='Day03/input.txt', mode='r') as file:
    lines = file.readlines()

    for n in range(100):
        arr = [[0]*128, [0]*128, [0]*128]
        for i in range(3):
                text = lines[n*3+i].strip()
                for x in text:
                    arr[i][ord(x)] = 1

        for i in range(128):
            if arr[0][i]==1 and arr[1][i]==1 and arr[2][i]==1:
                #print(text, chr(i))
                if ord('A') <= i <= ord('Z'):
                    pioritySum += (i - ord('A') + 27)
                else:
                    pioritySum += (i - ord('a') + 1)  

    print('-->', pioritySum)