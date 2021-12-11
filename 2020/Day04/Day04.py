import re


def main():
    # Part One: Report Valid Passports (Fields)
    passports = []
    with open('input.txt') as passport_input:
        new_passport = ''
        for line in passport_input:
            if line != '\n':
                new_passport += line.replace('\n', ' ')
            else:
                passports.append(new_passport.rstrip(' '))
                new_passport = ''
        if new_passport != '':
            passports.append(new_passport.rstrip(' '))
    # print(passports[0])
    count_valid = 0
    fields_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        field_dict = {}
        field_flag = True
        fields = passport.split(' ')
        for field in fields:
            key, value = field.split(':')
            field_dict[key] = value
        for key in fields_required:
            field_flag &= key in field_dict
        if field_flag:
            # print([f for f in field_dict])
            count_valid += 1
    print(count_valid)

    # Part Two: Report Valid Passports (Verification)
    count_valid = 0
    for passport in passports:
        validators = {'byr': val_byr,
                      'iyr': val_iyr,
                      'eyr': val_eyr,
                      'hgt': val_hgt,
                      'hcl': val_hcl,
                      'ecl': val_ecl,
                      'pid': val_pid}
        field_dict = {}
        field_flag = True
        fields = passport.split(' ')
        for field in fields:
            key, value = field.split(':')
            field_dict[key] = value
        for key in fields_required:
            field_flag &= key in field_dict
            if field_flag:
                field_flag &= validators[key](field_dict[key])
        if field_flag:
            count_valid += 1
    print(count_valid)


def val_byr(v):
    return 1920 <= int(v) <= 2002


def val_iyr(v):
    return 2010 <= int(v) <= 2020


def val_eyr(v):
    return 2020 <= int(v) <= 2030


def val_hgt(v):
    if v[-2:] not in ['in', 'cm']:
        return False
    if v[-2:] == 'in':
        return 59 <= int(v[:-2]) <= 76
    elif v[-2:] == 'cm':
        return 150 <= int(v[:-2]) <= 193


def val_hcl(v):
    m = re.search(r'#[0-9,a-f]{6}', v)
    return m is not None


def val_ecl(v):
    return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def val_pid(v):
    m = re.search(r'^\d{9}$', v)
    return m is not None


def val_cid(v):
    return True


if __name__ == '__main__':
    main()
