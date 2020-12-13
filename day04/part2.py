import re

expected_fields = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }
expected_eye_colors = { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }

def find_key(passport_field):
    return passport_field.split(':')[0]

leading_digits_regex = re.compile('[\d]+')

def is_valid_height(height):
    if height.endswith('cm'):
        heightValue = int(leading_digits_regex.match(height).group())
        return heightValue >= 150 and heightValue <= 193
    elif height.endswith('in'):
        heightValue = int(leading_digits_regex.match(height).group())
        return heightValue >= 59 and heightValue <= 76
    else:
        return False

color_regex = re.compile('#[0-9a-f]{6}$')
passport_id_regex = re.compile('[0-9]{9}$')

validators = {
    'byr': lambda x: len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: len(x) == 4 and int(x) >= 2010 and int(x) <= 2020,
    'eyr': lambda x: len(x) == 4 and int(x) >= 2020 and int(x) <= 2030,
    'hgt': is_valid_height,
    'hcl': lambda x: color_regex.match(x),
    'ecl': lambda x: x in expected_eye_colors,
    'pid': lambda x: passport_id_regex.match(x),
    'cid': lambda x: True
}

def is_valid(passport_string):
    fields = passport_string.split()
    keys = set([ find_key(field) for field in fields ])
    if not len(expected_fields.intersection(keys)) == len(expected_fields):
        return False
    for field in fields:
        blah = field.split(':')
        key = blah[0]
        value = blah[1]
        if not validators[key](value):
            return False
    return True

with open("input.txt") as input:
    passports = input.read().split('\n\n')
    valid_passports = filter(is_valid, passports)
    print(len(valid_passports))
