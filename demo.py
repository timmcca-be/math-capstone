import random

k = 5
p = 193


def eta(a, b):
    return [a ^ b, {m * k % p for m in a & b}]


def oplus(a, b):
    while len(b) != 0:
        [a, b] = eta(a, b)
    return a


def exponentiate(inputSet, exponent):
    resultSet = set()
    currentSet = inputSet
    while exponent > 0:
        if exponent % 2 == 0:
            currentSet = oplus(currentSet, currentSet)
            exponent /= 2
        else:
            resultSet = oplus(resultSet, currentSet)
            exponent -= 1
    return resultSet


def decode(key):
    return set((x + 1 for x in range(p - 1) if (1 << x) & key > 0))


def encode(inputSet):
    return sum((1 << (x - 1) for x in inputSet))


base = random.getrandbits(p - 1)
print('Base (shared by Alice and Bob):', base)
print('Base in binary:', '{0:b}'.format(base))
base_set = decode(base)
print('Base as set:', base_set)
print()

alice_exponent = random.getrandbits(p - 1)
print('Alice\'s secret exponent:', alice_exponent)
bob_exponent = random.getrandbits(p - 1)
print('Bob\'s secret exponent:', bob_exponent)
print()

alice_result = exponentiate(base_set, alice_exponent)
print('Alice\'s result set:', alice_result)
print('Alice sends Bob:', encode(alice_result))
bob_result = exponentiate(base_set, bob_exponent)
print('Bob\'s result set:', bob_result)
print('Bob sends Alice:', encode(bob_result))
print()

alice_final_result = exponentiate(bob_result, alice_exponent)
print('Alice\'s final result set:', alice_final_result)
alice_key = encode(alice_final_result)
print('Alice\'s key:', alice_key)
bob_final_result = exponentiate(alice_result, bob_exponent)
print('Bob\'s final result set:', bob_final_result)
bob_key = encode(bob_final_result)
print('Bob\'s key:', bob_key)
print()

if alice_key == bob_key:
    print('Success - Alice and Bob now share a secret key')
else:
    print('Failure - Alice and Bob ended up with different keys')
print()

print('Now, an attacker will try to determine the key from the non-secret information')
print('Hopefully, this will run indefinitely')
attacker_set = set()
attacker_exponent = 0
while attacker_set != alice_result:
    attacker_exponent += 1
    attacker_set = oplus(attacker_set, base_set)
print('Uh oh - the attacker has Alice\'s exponent or an equivalent')
print('Attacker exponent:', attacker_exponent)
print('The attacker will now try to compute the secret key')
print()

attacker_final_result = exponentiate(bob_result, attacker_exponent)
print('Attacker\'s final result set:', attacker_final_result)
attacker_key = encode(attacker_final_result)
print('Attacker\'s key:', attacker_key)
print()

if attacker_key == alice_key:
    print('The attacker got the final key')
else:
    print('The attacker\'s key is incorrect')
print()
