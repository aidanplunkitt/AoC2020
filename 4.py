import string

def validate_passport(passport):
    if not (1920 <= int(passport['byr']) <= 2002): return False
    if not (2010 <= int(passport['iyr']) <= 2020): return False
    if not (2020 <= int(passport['eyr']) <= 2030): return False
    ht = passport['hgt']
    if ht[-2:] != 'cm' and ht[-2:] != 'in': return False
    if ht[-2:] == 'cm':
        if not (150 <= int(ht[:-2]) <= 193): return False
    else: # in
        if not (59 <= int(ht[:-2]) <= 76): return False
    if passport['hcl'][0] != '#' or \
       any(c not in string.hexdigits for c in passport['hcl'][1:]): return False
    if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'): return False
    if len(passport['pid']) != 9 or not all(c in string.digits for c in passport['pid']): return False
    
    return True
    

count = 0
required_keys = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
found_keys = {}
with open('4.txt') as fp:
    for line in fp:
        line = line.rstrip()
        if not line:
            count = count + 1 if all(key in found_keys for key in required_keys) \
                                and validate_passport(found_keys) \
                    else count
            found_keys = {}
        else:
            found_keys.update(dict(e.split(':') for e in line.split(' ')))

# repeat for case of no ending newline in file
count = count + 1 if all(key in found_keys for key in required_keys) and validate_passport(found_keys) else count
print(count)