import random

def generate_random_set(modulus):
    return set(random.sample(range(0, modulus), random.randrange(0, modulus + 1)))

def eta(a, b, multiplier, modulus):
    return [a ^ b, {x * multiplier % modulus for x in a & b}]

def oplus(a, b, multiplier, modulus):
    while len(b) != 0:
        [a, b] = eta(a, b, multiplier, modulus)
    return a

def keyToSet(key, modulus):
    return set((x for x in range(modulus) if (1 << x) & key > 0))

def testMultiplier(multiplier, modulus):
    print('checking multiplier', multiplier, 'modulo', modulus)
    num_possible_sets = 2 << modulus
    for keyA in range(num_possible_sets):
        setA = keyToSet(keyA, modulus)
        for keyB in range(num_possible_sets):
            setB = keyToSet(keyB, modulus)
            aPlusB = oplus(setA, setB, multiplier, modulus)
            for keyC in range(num_possible_sets):
                setC = keyToSet(keyC, modulus)
                bPlusC = oplus(setB, setC, multiplier, modulus)
                if oplus(aPlusB, setC, multiplier, modulus) != oplus(setA, bPlusC, multiplier, modulus):
                    print(setA)
                    print(setB)
                    print(setC)
                    print('fail')
                    return
    print('success')
    return True

def testModulus(modulus):
    for multiplier in range(modulus):
        testMultiplier(multiplier, modulus)
