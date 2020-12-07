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
                num = int(bag.split()[-3])
                graph[container].append((contained, num))

# DFS search
def num_bags_inside(bag):
    if not graph[bag]:
        return 0

    total = 0
    for style, num in graph[bag]:
        total += num + (num_bags_inside(style) * num)
    return total

print(num_bags_inside('shiny gold'))