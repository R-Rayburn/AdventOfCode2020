import itertools

print('Corporate Policy')

min_ascii = 97
max_ascii = 122


def has_increasing_straight(password):
    pass_ascii = [ord(x) for x in password]
    differences = [str((pass_ascii[i] - pass_ascii[i + 1]) * -1) for i in range(len(pass_ascii) - 1)]
    if '111' in ''.join(differences):
        return True
    return False


def has_restricted_characters(password):
    return 'i' in password or 'o' in password or 'l' in password


# TODO: might have to pull out if a string of 3 exists
def has_two_different_non_overlapping_pairs(password):
    groupings = [x
                 for x in [''.join(g)
                           for _, g in itertools.groupby(password)]
                 if len(x) == 2]
    removed_dupes = list(dict.fromkeys(groupings))
    return len(removed_dupes) > 1


def meets_requirements(password):
    return has_increasing_straight(password) and\
           not has_restricted_characters(password) and\
           has_two_different_non_overlapping_pairs(password)


def format_password(password):
    i = password.find('i')
    o = password.find('o')
    l = password.find('l')
    highest = max([x for x in [i, o, l] if x > -1])
    string_to_replace = password[highest:]
    new_formatted_string = chr(ord(string_to_replace[0])+1) + ''.join(['a' for _ in range(len(string_to_replace[1:]))])
    return password.replace(string_to_replace, new_formatted_string)


# TODO: need to do a "reset" of all values up to value that is
def increment_password(password):
    # if has_restricted_characters(password):
    #     print(password)
    #     password = format_password(password)
    pass_ascii = [ord(x) for x in password]
    pass_ascii.reverse()
    pass_ascii[0] += 1
    while max_ascii in pass_ascii:
        i = pass_ascii.index(max_ascii)
        pass_ascii[i] = min_ascii
        pass_ascii[i+1] += 1
    pass_ascii.reverse()
    return ''.join([chr(x) for x in pass_ascii])


def retrieve_new_password(current_password):
    while not meets_requirements(current_password):
        current_password = increment_password(current_password)
    return current_password


print('Part 1')
print(f'Test 1: {retrieve_new_password("abcdefgh")}')
print(f'Test 2: {retrieve_new_password("ghijklmn")}')
# print(f'Data: {retrieve_new_password("1113122113", 40)}')
#
# print('Part 2')
# print(f'Data: {retrieve_new_password("1113122113", 50)}')
