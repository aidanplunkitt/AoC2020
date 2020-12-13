import math

_, buses = [line.strip() for line in open('13.txt')]
buses = [(dt, int(bus)) for dt, bus in enumerate(buses.split(',')) if bus != 'x']

# Fermat's little theorem
def inverse_mod(a, b):
    return pow(a, b-2, b)

result = 0
X = math.prod([bus[1] for bus in buses])
# Chinese remainder theorem
for dt, mod in buses:
    a_k = (mod - dt) % mod
    X_k = X // mod
    result += a_k * X_k * inverse_mod(X_k, mod)

print(result % X)