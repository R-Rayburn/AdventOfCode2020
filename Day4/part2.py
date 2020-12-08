import string
with open('data.txt', 'r') as f: lines = f.read()

expected_fields = [
    'byr', 'iyr',
    'eyr', 'hgt',
    'hcl', 'ecl',
    'pid'
]

class Passport:
    def __init__(self, data):
        self.data = data
    def byr_is_valid(self):
        lower_date = 1920
        upper_date = 2002
        return int(self.data['byr']) in range(lower_date, upper_date + 1)
    def iyr_is_valid(self):
        lower_date = 2010
        upper_date = 2020
        return int(self.data['iyr']) in range(lower_date, upper_date + 1)
    def eyr_is_valid(self):
        lower_date = 2020
        upper_date = 2030
        return int(self.data['eyr']) in range(lower_date, upper_date + 1)
    def hgt_is_valid(self):
        unit = self.data['hgt'][-2:]
        value = int(self.data['hgt'][:-2])
        cm_min = 150
        cm_max = 193
        in_min = 59
        in_max = 76
        return (unit == 'cm' and value in range(cm_min, cm_max + 1)) or (unit == 'in' and value in range(in_min, in_max+1))
    def hcl_is_valid(self):
        hash_sym = self.data['hcl'][:1]
        hash_val = self.data['hcl'][1:]
        return hash_sym == '#' and all(c in string.hexdigits for c in hash_val)
    def ecl_is_valid(self):
        colors = ['amb','blu','brn','gry','grn','hzl','oth']
        return self.data['ecl'] in colors
    def pid_is_valid(self):
        return len(self.data['pid']) == 9 and all(c in string.digits for c in self.data['pid'])

def validate_data(data):
    passport_data = Passport(data)
    return passport_data.byr_is_valid() and passport_data.iyr_is_valid() and passport_data.eyr_is_valid() and passport_data.hgt_is_valid() and passport_data.hcl_is_valid() and passport_data.ecl_is_valid() and passport_data.pid_is_valid()
        

def validate_passports(lines):
    passports = lines.split('\n\n')

    valid_passports = 0

    for passport in passports:
        passport_data = {}
        clean_pass = passport.replace('\n', ' ').split(' ')
        clean_pass = [i for i in clean_pass if i]
        print(clean_pass)
    
        for pass_data in clean_pass:
            key, value = pass_data.split(':')
            passport_data[key] = value
        if set(expected_fields).issubset(set(passport_data.keys())) and validate_data(passport_data):
            valid_passports += 1

    print(valid_passports)
    return valid_passports

validate_passports(lines)
