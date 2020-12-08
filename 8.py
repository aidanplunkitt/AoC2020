code = [line.strip() for line in open('8.txt')]

def execute(jmps_and_nops=[]):
    visited = addr = acc = 0
    while not ((1 << addr) & visited) and addr < len(code):
        instr, data = code[addr].split()
        if instr == 'acc':
            acc += int(data)
        else:
            jmps_and_nops.append((addr, instr, data))

        visited |= 1 << addr
        addr += int(data) if instr == 'jmp' else 1

    return addr, acc

# populate list of candidate ops to edit
init_jmps_and_nops = []
execute(init_jmps_and_nops)

# bruteforce
acc = 0
swap = {'jmp':'nop', 'nop':'jmp'}
for addr, instr, data in init_jmps_and_nops:
    orig = code[addr]
    code[addr] = ' '.join([swap[instr], data])
    final_addr, acc = execute()
    if final_addr == len(code):
        break
    code[addr] = orig

print(acc)