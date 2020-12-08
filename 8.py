code = [line.strip() for line in open('8.txt')]

acc = [0] # list to force global var
def execute(addr):
    instr, data = code[addr].split()
    if instr == 'acc':
        acc[0] += int(data)

    return addr + (int(data) if instr == 'jmp' else 1)

visited = address = 0
while not ((1 << address) & visited):
    visited |= 1 << address
    address = execute(address)

print(acc[0])