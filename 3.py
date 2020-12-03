tree_count = 0
with open('3.txt') as fp:
    pos = 0
    for line in fp:
        line = line.rstrip()
        if line[pos] == '#':
            tree_count += 1
        pos = (pos + 3) % len(line)

print(tree_count)