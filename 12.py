DIR_MAP = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1,0)}
waypoint = [10,1]
ship     = [0,0]
with open('12.txt') as fp:
    for line in fp:
        line = line.strip()
        op = line[0]
        num = int(line[1:])
        if op in 'LR':
            rot = num // 90
            for i in range(rot):
                if op == 'L': 
                    waypoint = [-waypoint[1]] + [waypoint[0]]
                else:
                    waypoint = [waypoint[1]] + [-waypoint[0]]
            continue
        
        if op == 'F':
            for i in range(2):
                ship[i] += num * waypoint[i]
            continue

        for i in range(2):
            waypoint[i] += num * DIR_MAP[op][i]

print(abs(ship[0]) + abs(ship[1]))