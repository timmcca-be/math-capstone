import random

def generate_random_set(modulus, size = None):
    if size == None:
        size = random.randrange(1, modulus)
    return frozenset(random.sample(range(1, modulus), size))

def eta(a, b, multiplier, modulus):
    return [a ^ b, {x * multiplier % modulus for x in a & b}]

def oplus(a, b, multiplier, modulus):
    while len(b) != 0:
        [a, b] = eta(a, b, multiplier, modulus)
    return a

def findOrder(start, multiplier, modulus):
    order = 1
    visited = set()
    current = start
    while current not in visited:
        visited.add(current)
        current = oplus(current, start, multiplier, modulus)
        order += 1
    return order

def isPowerOfTwo(num):
    while num % 2 == 0:
        num //= 2
    return num == 1

# for modulus in range(1, 20):
#     for multiplier in range(0, modulus):
#         orders = [findOrder(generate_random_set(modulus), multiplier, modulus) for _ in range(1000)]
#         if max(orders) == 2 ** (modulus - 1):
#             print(max(orders), sum(orders) / 1000, len([num for num in orders if not isPowerOfTwo(num)]), end = ',')
#     print()
