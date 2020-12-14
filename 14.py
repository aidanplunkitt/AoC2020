def apply_mask(num, mask):
    for i in range(len(mask)):
        if mask[35-i] != 'X':
            if mask[35-i] == '1':
                num |= 1 << i
            else:
                num &= ~(1 << i)
    return num

d= {}
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
with open('14.txt') as fp:
    for line in fp:
        line = line.strip().split(" = ")
        if line[0] == 'mask':
            mask = line[1]
        else:
            d[line[0]] = apply_mask(int(line[1]), mask)

print(sum(d.values()))