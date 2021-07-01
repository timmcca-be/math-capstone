import random

modulus = 127
multiplier = 2

def generate_random_set():
    return set(random.sample(range(0, modulus), random.randrange(0, modulus + 1)))

def eta(a, b):
    return [a ^ b, {x * multiplier % modulus for x in a & b}]

def oplus(a, b):
    while len(b) != 0:
        [a, b] = eta(a, b)
    return a

for i in range(100000):
    a = generate_random_set()
    b = generate_random_set()
    c = generate_random_set()
    if oplus(oplus(a, b), c) != oplus(a, oplus(b, c)):
        print('fail')
        break
