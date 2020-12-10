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

# first two elements are padding to avoid index errors, 
# and the 1 at cache[2] represents the 1 arrangement for 0 jolts from the outlet
cache = [0,0,1] + [0] * adapters[-1]
for a in adapters:
    # a=1 corresponds to cache[3], so +2
    i = a + 2
    cache[i] = sum(cache[i-3:i])

# p2 answer
print(cache[-1])
