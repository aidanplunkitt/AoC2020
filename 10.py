adapters = [int(line.strip()) for line in open('10.txt').readlines()]
adapters.sort()
diffs = [0] * 4
jolts = 0
for a in adapters:
    diffs[a-jolts] += 1
    jolts = a

diffs[3] += 1 # for device's built-in adapter

# p1 answer
print(diffs[1] * diffs[3])