import collections

# build DAG
graph = collections.defaultdict(list)
with open('7.txt') as fp:
    for line in fp:
        bag_types = line.split('bag')
        container = ' '.join(bag_types[0].split()[:2])
        for bag in bag_types[1:-1]:
            contained = ' '.join(bag.split()[-2:])
            if contained != 'no other':
                graph[contained].append(container)

# run BFS
s = set()
q = collections.deque()
q.extend(graph['shiny gold'])
while q:
    node = q.popleft()
    s.add(node)
    q.extend(graph[node])

print(len(s))