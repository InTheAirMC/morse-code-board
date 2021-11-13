import random
#random.randrange(0,3)
lst = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
stop_range = 0
for x in range(100):
    lst.append([])
    for y in range(4):
#         print(lst)
        if lst[x][y] == 0: #if last bit is 0
            if stop_range < 2 and random.randrange(0,3) == 0:
                if random.randrange(0,5) != 0: #add 1,2
                    lst[x+1].append(1)
                else:
                    lst[x+1].append(2)
                stop_range += 1
            else:
                lst[x+1].append(0)
        elif lst[x][y] == 1: # if last bit is 1
            stop_range -= 1
            lst[x+1].append(0)
        elif lst[x][y] == 2: # if last bit is 2
            if lst[x-1][y] != 2:
                lst[x+1].append(2)
            elif random.randrange(0,3) != 0:
                lst[x+1].append(2)
            else:
                stop_range -= 1
                lst[x+1].append(0)

for x in lst:
    print(x)
