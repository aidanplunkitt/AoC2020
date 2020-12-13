_, buses = [line.strip() for line in open('13.txt')]
buses = [(pos, int(bus)) for pos, bus in enumerate(buses.split(',')) if bus != 'x']
print(buses)
time = 0
while True:
    if all([(time + pos) % bus == 0 for pos, bus in buses]):
        print(time)
        break
    time += buses[0][1]