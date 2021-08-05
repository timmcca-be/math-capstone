import random


def generate_random_set(modulus, size):
    return frozenset(random.sample(range(1, modulus), size))


def eta(a, b, multiplier, modulus):
    return [a ^ b, {x * multiplier % modulus for x in a & b}]


def oplus(a, b, multiplier, modulus):
    while len(b) != 0:
        [a, b] = eta(a, b, multiplier, modulus)
    return a


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def euler_phi(value):
    return sum(1 for i in range(1, value) if gcd(value, i) == 1)


def find_number_order(value, modulus):
    order = 1
    current = value
    while current != 1:
        current = current * value % modulus
        order += 1
    return order


def find_primitive_roots(modulus):
    phi = euler_phi(modulus)
    return [i for i in range(2, modulus) if find_number_order(i, modulus) == phi]


def find_set_order(start, multiplier, modulus):
    order = 1
    visited = set()
    current = start
    while current not in visited:
        visited.add(current)
        current = oplus(current, start, multiplier, modulus)
        order += 1
    return order


def exponentiate(start, power, multiplier, modulus):
    result = set()
    current = start
    while power > 0:
        if power % 2 == 0:
            current = oplus(current, current, multiplier, modulus)
            power /= 2
        else:
            result = oplus(result, current, multiplier, modulus)
            power -= 1
    return result


def check(p, k):
    for size in range(1, p - 1):
        for _ in range(100):
            order = find_set_order(generate_random_set(p, size), k, p)
            print(p, end=',')
            print(k, end=',')
            print(size, end=',')
            print(order)


primes = [2, 3, 5, 7, 11, 13]
print('p,k,size,order')
# for p in primes:
#     for k in find_primitive_roots(p):
#         check(p, k)
# check(17, 3)
