class Field:
    def __init__(self, name, ranges):
        self.name = name
        self.ranges = tuple([tuple(r) for r in ranges])

    def __repr__(self):
        return ' '.join([self.name, str(self.ranges)])

field_info, my_ticket, tickets = [line.split('\n') for line in open('16.txt').read().split('\n\n')]
max_val = 0
fields = []
for i, field in enumerate(field_info):
    *name, a, _, b = field.split(' ')
    name = ' '.join(name).strip(':')
    ranges = [[int(n) for n in r.split('-')] for r in (a, b)]
    fields.append(Field(name, ranges))
    max_val = max(max_val, ranges[0][1], ranges[1][1])
    
valid = [False] * (max_val + 1)
for f in fields:
    for start, end in f.ranges:
        valid[start:end+1] = [True for _ in range(start, end+1)]

error_rate = 0
t_matrix = []
for ticket in tickets[1:]:
    if ticket:
        values = [int(n) for n in ticket.split(',')]
        if error := sum(v for v in values if v > max_val or not valid[v]):
            error_rate += error
        else:
            t_matrix.append(values)
# p1 answer
print(error_rate)

potential = [[0, set(), i] for i in range(len(t_matrix[0]))]
for col in range(len(potential)):
    for field in fields:
        if all([field.ranges[0][0] <= t_matrix[n][col] <= field.ranges[0][1] or \
                field.ranges[1][0] <= t_matrix[n][col] <= field.ranges[1][1] \
                for n in range(len(t_matrix))]):
            potential[col][0] += 1
            potential[col][1].add(field.name)

product = 1
assigned = set()
potential.sort(key=lambda x: x[0])
my_ticket = [int(n) for n in my_ticket[1].split(',')]
for i in range(len(t_matrix[0])):
    p_set = potential[i][1]
    f = p_set.difference(assigned).pop()
    assigned.add(f)
    if f.split()[0] == 'departure':
        product *= my_ticket[potential[i][2]]

# p2 answer
print(product)