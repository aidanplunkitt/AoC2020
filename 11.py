def count_occupied(A):
    count = 0
    for row in A:
        for seat in row:
            if seat == '#':
                count += 1
    return count


def seat_counts(A):
    cache = [[0] * len(A[0]) for _ in A]

    for i, row in enumerate(A):
        for j, seat in enumerate(row):
            if seat == '.': continue

            neighbors = []
            # down
            i_ = i + 1
            while i_ < len(A):
                if A[i_][j] != '.':
                    neighbors.append((i_, j))
                    break
                i_ += 1
            # up
            i_ = i - 1
            while i_ >= 0:
                if A[i_][j] != '.':
                    neighbors.append((i_, j))
                    break
                i_ -= 1
            # right
            j_ = j + 1
            while j_ < len(A[0]):
                if A[i][j_] != '.':
                    neighbors.append((i, j_))
                    break
                j_ += 1
            # left
            j_ = j - 1
            while j_ >= 0:
                if A[i][j_] != '.':
                    neighbors.append((i, j_))
                    break
                j_ -= 1
            # NW diag
            i_, j_ = i - 1, j - 1
            while i_ >= 0 and j_ >= 0:
                if A[i_][j_] != '.':
                    neighbors.append((i_, j_))
                    break
                i_, j_ = i_ - 1, j_ - 1
            # NE diag
            i_, j_ = i - 1, j + 1
            while i_ >= 0 and j_ < len(A[0]):
                if A[i_][j_] != '.':
                    neighbors.append((i_, j_))
                    break
                i_, j_ = i_ - 1, j_ + 1
            # SW diag
            i_, j_ = i + 1, j - 1
            while i_ < len(A) and j_ >= 0:
                if A[i_][j_] != '.':
                    neighbors.append((i_, j_))
                    break
                i_, j_ = i_ + 1, j_ - 1
            # SE diag
            i_, j_ = i + 1, j + 1
            while i_ < len(A) and j_ < len(A[0]):
                if A[i_][j_] != '.':
                    neighbors.append((i_, j_))
                    break
                i_, j_ = i_ + 1, j_ + 1

            occupied_neighbors = 0
            for x, y in neighbors:
                if A[x][y] == '#':
                    occupied_neighbors += 1
            cache[i][j] = occupied_neighbors

    return cache


def change_seat(occupied_neighbors, status):
    if status == 'L' and occupied_neighbors == 0:
        return '#'

    if status == '#' and occupied_neighbors >= 5:
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

print(count_occupied(seats))