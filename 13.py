departure, buses = [line.strip() for line in open('13.txt')]
departure = int(departure)
buses = [int(bus) for bus in buses.split(',') if bus != 'x']

mintime, ans1 = departure, 0
for bus in buses:
    if (wait := bus - (departure % bus)) < mintime:
        mintime, ans1 = wait, bus * wait

print(ans1)