def apply_mask(addr, mask):
    addrs = [addr]
    for i in range(len(mask)):
        if mask[35-i] == '1':
            addrs = [addr | (1 << i) for addr in addrs]
        if mask[35-i] == 'X':
            tmp = []
            while addrs:
                a = addrs.pop()
                tmp.append(a & ~(1 << i)) # set X to 0
                tmp.append(a |  (1 << i)) # set X to 1
            addrs = tmp
            
    return addrs

d= {}
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
with open('14.txt') as fp:
    for line in fp:
        line = line.strip().split(" = ")
        if line[0] == 'mask':
            mask = line[1]
        else:
            addr = int(line[0][4:].rstrip(']'))
            for a in apply_mask(addr, mask):
                d[a] = int(line[1])

print(sum(d.values()))