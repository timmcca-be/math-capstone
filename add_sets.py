import random

def generate_random_set():
    return set(random.sample(range(-10, 10), random.randrange(5, 16)))

def add_sets(a, b, k):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    union = a | b
    intersection = a & b
    return add_sets(union - intersection, {k * x for x in intersection}, k)


# print(a)
# print(b)
# print(add_sets(a, b, -1))
for i in range(100000):
    a = generate_random_set()
    b = generate_random_set()
    c = generate_random_set()
    if add_sets(add_sets(a, b, -1), c, -1) != add_sets(a, add_sets(b, c, -1), -1):
        print('fail')
