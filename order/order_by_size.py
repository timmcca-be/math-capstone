from order import *

MODULUS = 13
MULTIPLIER = 7

TEST_COUNT = 10000

def exponentiate(inputSet, exponent):
    resultSet = set()
    currentSet = inputSet
    while exponent > 0:
        if exponent % 2 == 0:
            currentSet = oplus(currentSet, currentSet, MULTIPLIER, MODULUS)
            exponent /= 2
        else:
            resultSet = oplus(resultSet, currentSet, MULTIPLIER, MODULUS)
            exponent -= 1
    return resultSet

orders = set()
for _ in range(TEST_COUNT):
    orders.add(findOrder(generate_random_set(MODULUS), MULTIPLIER, MODULUS))

orders_list = list(orders)
orders_list.sort()
print(orders_list)
