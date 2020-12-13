expected_fields = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }

def find_key(passport_field):
    return passport_field.split(':')[0]

def is_valid(passport_string):
    fields = passport_string.split()
    keys = set([ find_key(field) for field in fields ])
    return len(expected_fields.intersection(keys)) == len(expected_fields)

with open("input.txt") as input:
    passports = input.read().split('\n\n')
    valid_passports = filter(is_valid, passports)
    print(len(valid_passports))
