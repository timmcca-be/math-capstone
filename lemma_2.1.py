import random

def generate_random_set():
    return set(random.sample(range(-10, 10), random.randrange(5, 16)))

def eta(a, b, k = 2):
    union = a | b
    intersection = a & b
    return [union - intersection, {k * x for x in intersection}]

def eta_n(k, n, a, b):
    for _ in range(n):
        [a, b] = eta(k, a, b)
    return [a, b]

def rimu(a, b, k = 2):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    return rimu(a ^ b, {k * x for x in a & b}, k)

for i in range(100000):
    a = generate_random_set()
    b = generate_random_set()
    c = generate_random_set()
    if eta(eta(a, b)[0], c)[0] != eta(a, eta(b, c)[0])[0]:
        print('fail')
    b1 = set()
    b2 = set()
    for item in b:
        if random.random() > 0.5:
            b1.add(item)
        else:
            b2.add(item)
    if rimu(rimu(a, b), c) != rimu(rimu(a, b2), rimu(b1, c)):
        print('fail2')
