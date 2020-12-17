import itertools

deltas = list(itertools.product([-1,0,1], repeat=3))
deltas.remove((0,0,0))

initial = '''
.##...#.
.#.###..
..##.#.#
##...#.#
#..#...#
#..###..
.##.####
..#####.
'''

lines = [line for line in initial.split('\n') if line]
active = set([(i, j, 0) for i, line in enumerate(lines) for j, x in enumerate(line) if x == '#'])

for i in range(6):
    new_active = set()
    unactive = set()

    # add unchanged active
    for a in active:
        x, y, z = a
        active_neighbors = 0
        for dx, dy, dz in deltas:
            if (p := (x+dx, y+dy, z+dz)) in active:
                active_neighbors += 1
            else:
                unactive.add(p)
        if 2 <= active_neighbors <= 3:
            new_active.add(a)

    # check potential unactive -> active
    for u in unactive:
        x, y, z = u
        active_neighbors = 0
        for dx, dy, dz in deltas:
            if p := (x+dx, y+dy, z+dz) in active:
                active_neighbors += 1
        if active_neighbors == 3:
            new_active.add(u)

    active = new_active

# p1 answer
print(len(active))