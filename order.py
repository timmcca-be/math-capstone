import random

def generate_random_set(modulus):
    return frozenset(random.sample(range(0, modulus), random.randrange(0, modulus + 1)))

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

for modulus in range(1, 20):
    for multiplier in range(0, modulus):
        print(max(findOrder(generate_random_set(modulus), multiplier, modulus) for _ in range(100)), end = ',')
    print()
