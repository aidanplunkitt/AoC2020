import string

s = set()
s.update(c for c in string.ascii_lowercase)
group_sum = 0

with open('6.txt') as fp:
    for line in fp:
        line = line.strip()
        if line:
            s.intersection_update(c for c in line)
        else:
            group_sum += len(s)
            s.update(c for c in string.ascii_lowercase)

print(group_sum + len(s))