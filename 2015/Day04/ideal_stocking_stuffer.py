import hashlib
print('The Ideal Stocking Stuffer')
secret_key = 'bgvyzdsv'


def find_md5_hash(secret, zero_size):
    num = 1
    while True:
        my_hex = hashlib.md5((secret + str(num)).encode())
        if str(my_hex.hexdigest())[:len(zero_size)] == zero_size:
            return num, my_hex.hexdigest()
        else:
            num += 1


print('Part 1')
print(f'Test 1: {find_md5_hash("abcdef", "00000")}')  # 609043
print(f'Test 2: {find_md5_hash("pqrstuv", "00000")}')  # 1048970
print(f'Data: {find_md5_hash(secret_key, "00000")}')

print(hashlib.md5(secret_key.encode()).hexdigest())
print(hashlib.md5(str(254575).encode()).hexdigest())

print('Part 2')
print(f'Data: {find_md5_hash(secret_key, "000000")}')
