s = set()
with open('1.txt') as fp:
    for num in fp:
        num = int(num)
        if num in s:
            print(num * (2020 - num))
            break
        else:
            s.add(2020 - num)