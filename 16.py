fields, my_ticket, tickets = [line.split('\n') for line in open('16.txt').read().split('\n\n')]
ranges = []
for field in fields:
    a, _, b = field.split(' ')[-3:]
    ranges.extend([[int(n) for n in r.split('-')] for r in (a, b)])
ranges.sort(key=lambda x: x[1])
valid = [False] * (ranges[-1][1] + 1)
for start, end in ranges:
    valid[start:end+1] = [True for _ in range(start, end+1)]

error_rate = 0
for ticket in tickets[1:]:
    if ticket:
        values = [int(n) for n in ticket.split(',')]
        error_rate += sum(v for v in values if v >= len(valid) or not valid[v])

# p1 answer
print(error_rate)