def count_occupied(A):
    count = 0
    for row in A:
        for seat in row:
            if seat == '#':
                count += 1
    return count


def seat_counts(A):
    cache = [[0] * len(A[0]) for _ in A]

    # fill inner matrix first, skipping borders
    for i in range(1, len(A) - 1):
        for j in range(1, len(A[0]) - 1):
            if A[i][j] == '#':
                for i_ in range(i-1, i+2):
                    for j_ in range(j-1, j+2):
                        cache[i_][j_] += 1
                # exclude the cell itself
                cache[i][j] -= 1

    # now do borders w/o corners
    # top and bottom
    for j in range(1, len(A[0]) - 1):
        if A[0][j] == '#':
            for i_ in range(0, 2):
                for j_ in range(j-1, j+2):
                    cache[i_][j_] += 1
            cache[0][j] -=1
        if A[-1][j] == '#':
            for i_ in range(len(A) - 2, len(A)):
                for j_ in range(j-1, j+2):
                    cache[i_][j_] += 1
            cache[-1][j] -=1
    # left and right
    for i in range(1, len(A) - 1):
        if A[i][0] == '#':
            for i_ in range(i-1, i+2):
                for j_ in range(0, 2):
                    cache[i_][j_] += 1
            cache[i][0] -= 1
        if A[i][-1] == '#':
            for i_ in range(i-1, i+2):
                for j_ in range(len(A[0]) - 2, len(A[0])):
                    cache[i_][j_] += 1
            cache[i][-1] -= 1

    # corners (note this fails for matrices with a side <= 2)
    if A[0][0] == '#':
        cache[0][1] += 1
        cache[1][0] += 1
        cache[1][1] += 1
    if A[0][-1] == '#':
        cache[0][-2] += 1
        cache[1][-1] += 1
        cache[1][-2] += 1
    if A[-1][0] == '#':
        cache[-1][1] += 1
        cache[-2][0] += 1
        cache[-2][1] += 1
    if A[-1][-1] == '#':
        cache[-1][-2] += 1
        cache[-2][-2] += 1
        cache[-2][-1] += 1

    return cache


def change_seat(occupied_neighbors, status):
    if status == 'L' and occupied_neighbors == 0:
        return '#'

    if status == '#' and occupied_neighbors >= 4:
        return 'L'

    return None


seats = [[c for c in line.strip()] for line in open('11.txt')]
changes = True
while changes:
    changes = False
    cache = seat_counts(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if new_seat := change_seat(cache[i][j], seat):
                seats[i][j] = new_seat
                changes = True
# p1 answer
print(count_occupied(seats))