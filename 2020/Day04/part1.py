with open('data.txt', 'r') as f: lines = f.read()

expected_fields = [
    'byr', 'iyr',
    'eyr', 'hgt',
    'hcl', 'ecl',
    'pid'
]

def validate_passports(lines):
    passports = lines.split('\n\n')

    valid_passports = 0

    for passport in passports:
        passport_keys = []
        clean_pass = passport.replace('\n', ' ').split(' ')
        clean_pass = [i for i in clean_pass if i]
        print(clean_pass)
    
        for pass_data in clean_pass:
            key, _ = pass_data.split(':')
            passport_keys.append(key)
        if set(expected_fields).issubset(set(passport_keys)):
            valid_passports += 1

    print(valid_passports)
    return valid_passports

validate_passports(lines)
