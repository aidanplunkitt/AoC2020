num_valid = 0
with open('2.txt') as fp:
    for line in fp:
        dash = 1
        while line[dash] != '-':
            dash += 1
        space = dash + 2
        while line[space] != ' ':
            space += 1

        minnum = int(line[0:dash])
        maxnum = int(line[dash+1:space])
        char = line[space+1]
        search_string = (line[space+4:]).rstrip()

        count = 0
        for c in search_string:
            if c is char:
                count += 1

        if minnum <= count <= maxnum:
            num_valid += 1

print(num_valid)