STARTING = [12,20,0,6,1,17,7]
heard = {n: turn+1 for turn, n in enumerate(STARTING[:-1])}

last_spoken = STARTING[-1]
for turn in range(len(STARTING), 30000000):
    next_to_speak = 0 if last_spoken not in heard else turn - heard[last_spoken]
    heard[last_spoken] = turn
    last_spoken = next_to_speak

print(last_spoken)