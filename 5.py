import functools

def calc_seat_id(s):
    # row = 0
    # for i in line[:7]:
    #     row <<= 1
    #     if i == 'B':
    #         row += 1
    # col = 0
    # for i in line[7:10]:
    #     col <<= 1
    #     if i == 'R':
    #         col += 1
    # return row * 8 + col
    return functools.reduce(lambda x, y: (x << 1) + int(y == 'B' or y == 'R'), line[:10], 0)

max_id = -1
with open('5.txt') as fp:
    for line in fp:
        seat_id = functools.reduce(lambda x, y: (x << 1) + int(y == 'B' or y == 'R'), line[:10], 0)
        max_id = max(max_id, seat_id)
print(max_id)