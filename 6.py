import string

s = set()
group_sum = 0

with open('6.txt') as fp:
    for line in fp:
        line = line.strip()
        if line:
            s.update(c for c in line)
        else:
            group_sum += len(s)
            s.clear()

print(group_sum + len(s))