count = 0
required_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
found_keys = {}
with open('4.txt') as fp:
    for line in fp:
        line = line.rstrip()
        if not line:
            count = count + 1 if all(key in found_keys for key in required_keys) else count
            found_keys = {}
        else:
            found_keys.update(dict(e.split(':') for e in line.split(' ')))

# repeat for case of no ending newline in file
count = count + 1 if all(key in found_keys for key in required_keys) else count
print(count)