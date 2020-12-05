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
    return functools.reduce(lambda x, y: (x << 1) + int(y in 'RB'), line[:10], 0)

seats = [0] * 2**10
with open('5.txt') as fp:
    for line in fp:
        seat_id = functools.reduce(lambda x, y: (x << 1) + int(y in 'RB'), line[:10], 0)
        seats[seat_id] = 1

my_seat = [i+1 for i, seat in enumerate(seats[1:-2]) if not seat and seats[i] and seats[i+2]]
print(my_seat[0])