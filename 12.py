DIR_MAP = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1,0)}
COMPASS = ['N', 'E', 'S', 'W']
direction = 'E'
location = [0,0]
with open('12.txt') as fp:
    for line in fp:
        line = line.strip()
        op = line[0]
        num = int(line[1:])
        if op in 'LR':
            rot = num // 90
            rot *= -1 if op == 'L' else 1
            direction = COMPASS[(COMPASS.index(direction) + rot) % 4]
            continue
        
        curr_dir = direction if op == 'F' else op
        for i in range(2):
            location[i] += num * DIR_MAP[curr_dir][i]

# p1 answer
print(abs(location[0]) + abs(location[1]))