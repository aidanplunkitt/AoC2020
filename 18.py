from collections import deque
import math

ops = {'+': lambda x, y: x+y,
       '*': lambda x, y: x*y}

def solve(i):
    nums, symbols = deque(), deque()
    while i < len(expression):
        c = expression[i]
        if c == ' ':
            i += 1
            continue
        elif c == '(':
            i, val = solve(i + 1)
            nums.append(val)
        elif c == ')':
            break
        elif c in '+*':
            symbols.append(c)
        else: # digit
            nums.append(int(c))
        i += 1

    multiplicands = [nums.popleft()]
    for op in symbols:
        num = nums.popleft()
        if op == '+':
            num += multiplicands.pop()
        multiplicands.append(num)

    return i, math.prod(multiplicands)

result = 0
for expression in open('18.txt').read().splitlines():
        result += solve(0)[1]
print(result)