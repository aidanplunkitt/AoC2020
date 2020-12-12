import collections

PREAMBLE_SIZE = 25

invalid = 0
q = collections.deque()
with open('9.txt') as fp:
    for i in range(PREAMBLE_SIZE):
        q.append(int(fp.readline().strip()))

    for line in fp:
        curr = int(line.strip())
        hashset = set()
        valid = False
        for num in q:
            if num in hashset: # valid
                valid = True
                break
            hashset.add(curr - num)

        if not valid:
            invalid = curr
            break

        q.popleft()
        q.append(curr)

# part 1
print(invalid)

q.clear()
qsum = 0
with open('9.txt') as fp:
    while qsum != invalid:
        while qsum < invalid:
            data = int(fp.readline().strip())
            q.append(data)
            qsum += data

        while qsum > invalid:
            qsum -= q.popleft()

# part 2
encryption_weakness = min(q) + max(q)
print(encryption_weakness)