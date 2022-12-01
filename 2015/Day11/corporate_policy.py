# To help him remember his new password after the old one expires,
# Santa has devised a method of coming up with a password based on the previous one. 
# Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), 
# so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. 
# Increase the rightmost letter one step; if it was z, it wraps around to a, 
# and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.




import itertools
import string

print('Corporate Policy')

MIN_ASCII = 97
OUT_OF_RANGE_ASCII = 123
MAX_ASCII = 122
MAX_LEN = 8


def has_restricted_letters(password):
    return 'i' in password or 'o' in password or 'l' in password


# Does this need to be strictly one?
def has_increasing_straight(password):
    alpha = string.ascii_lowercase
    increasing_straights = [alpha[i:i+3] for i in range(len(alpha[:-3])) if not has_restricted_letters(alpha[i:i+3])]
    return any(s in password for s in increasing_straights)


def has_two_different_non_overlapping_pairs(password):
    pairs = {i:password[i:i+2] for i in range(len(password)-1)}
    dupe_indexes = [i for i in pairs.keys() if pairs[i][0] == pairs[i][1]]
    if len(dupe_indexes) > 2 or (len(dupe_indexes) == 2 and abs(dupe_indexes[0] - dupe_indexes[1]) != 1):
        return True
    return False


def meets_requirements(password):
    return not has_restricted_letters(password) and\
        has_increasing_straight(password) and\
        has_two_different_non_overlapping_pairs(password)


def increment_password(password):
    print(password)
    pass_ascii = [ord(x) for x in password]
    pass_ascii.reverse()
    pass_ascii[0] += 1
    while OUT_OF_RANGE_ASCII in pass_ascii:
        i = pass_ascii.index(OUT_OF_RANGE_ASCII)
        pass_ascii[i] = MIN_ASCII
        pass_ascii[i+1] += 1
    pass_ascii.reverse()
    return ''.join([chr(x) for x in pass_ascii])
    

def retrieve_new_password(current_password):
    while not meets_requirements(current_password):
        current_password = increment_password(current_password)
    return current_password



# def has_increasing_straight(password):
#     pass_ascii = [ord(x) for x in password]
#     differences = [str((pass_ascii[i] - pass_ascii[i + 1]) * -1) for i in range(len(pass_ascii) - 1)]
#     if '111' in ''.join(differences):
#         return True
#     return False


# def has_restricted_characters(password):
#     return 'i' in password or 'o' in password or 'l' in password


# # TODO: might have to pull out if a string of 3 exists
# def has_two_different_non_overlapping_pairs(password):
#     groupings = [x
#                  for x in [''.join(g)
#                            for _, g in itertools.groupby(password)]
#                  if len(x) == 2]
#     removed_dupes = list(dict.fromkeys(groupings))
#     return len(removed_dupes) > 1


# def meets_requirements(password):
#     return has_increasing_straight(password) and\
#            not has_restricted_characters(password) and\
#            has_two_different_non_overlapping_pairs(password)


# def format_password(password):
#     i = password.find('i')
#     o = password.find('o')
#     l = password.find('l')
#     highest = max([x for x in [i, o, l] if x > -1])
#     string_to_replace = password[highest:]
#     new_formatted_string = chr(ord(string_to_replace[0])+1) + ''.join(['a' for _ in range(len(string_to_replace[1:]))])
#     return password.replace(string_to_replace, new_formatted_string)


# # TODO: need to do a "reset" of all values up to value that is
# def increment_password(password):
#     # if has_restricted_characters(password):
#     #     print(password)
#     #     password = format_password(password)
#     pass_ascii = [ord(x) for x in password]
#     pass_ascii.reverse()
#     pass_ascii[0] += 1
#     while max_ascii in pass_ascii:
#         i = pass_ascii.index(max_ascii)
#         pass_ascii[i] = min_ascii
#         pass_ascii[i+1] += 1
#     pass_ascii.reverse()
#     return ''.join([chr(x) for x in pass_ascii])


# def retrieve_new_password(current_password):
#     while not meets_requirements(current_password):
#         current_password = increment_password(current_password)
#     return current_password


print('Part 1')
# print(f'Test 1: {retrieve_new_password("abcdefgh")}')
# print(f'Test 2: {retrieve_new_password("ghijklmn")}')
print(f'Data: {retrieve_new_password("cqjxjnds")}')  # This is not correct still. Test values pass though. Need to see where the logic is wrong.
# #
# # print('Part 2')
# # print(f'Data: {retrieve_new_password("1113122113", 50)}')
