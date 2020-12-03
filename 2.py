num_valid = 0
with open('2.txt') as fp:
    for line in fp:
        dash = 1
        while line[dash] != '-':
            dash += 1
        space = dash + 2
        while line[space] != ' ':
            space += 1

        idx1 = int(line[0:dash]) - 1
        idx2 = int(line[dash+1:space]) - 1
        char = line[space+1]
        search_string = (line[space+4:]).rstrip()

        if search_string[idx1] is char:
            if search_string[idx2] is not char:
                num_valid += 1
        elif search_string[idx2] is char:
            num_valid += 1

print(num_valid)