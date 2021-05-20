import random

def generate_random_set():
    return set(random.sample(range(-10, 10), random.randrange(5, 16)))

def eta(a, b, k = 2):
    return [a ^ b, {k * x for x in a & b}]

def eta_n(n, a, b, k = 2):
    for _ in range(n):
        [a, b] = eta(a, b, k)
    return [a, b]

def rimu(a, b, k = 2):
    while len(b) != 0:
        [a, b] = eta(a, b, k)
    return a

for i in range(100000):
    a = generate_random_set()
    b = generate_random_set()
    c = generate_random_set()
    if rimu(rimu(a, b), c) != rimu(a, rimu(b, c)):
        print('fail')
