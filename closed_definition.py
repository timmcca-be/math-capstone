import random

def generate_random_set(modulus):
    return set(random.sample(range(0, modulus), random.randrange(0, modulus + 1)))

def oplus_new(a, b, multiplier, modulus):
    result = a.copy()
    for item in b:
        while item in result:
            result.remove(item)
            item = item * multiplier % modulus
        result.add(item)
    return result

def eta(a, b, multiplier, modulus):
    return [a ^ b, {x * multiplier % modulus for x in a & b}]

def oplus_old(a, b, multiplier, modulus):
    while len(b) != 0:
        [a, b] = eta(a, b, multiplier, modulus)
    return a

for i in range(100000):
    a = generate_random_set(11)
    b = generate_random_set(11)
    if oplus_old(a, b, 2, 11) != oplus_new(a, b, 2, 11):
        print('fail')
        break
