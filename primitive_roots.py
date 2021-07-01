def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

totient_memo = dict()
def euler_totient(modulus):
    if modulus in totient_memo:
        return totient_memo[modulus]
    totient = sum(1 for number in range(modulus) if number != 0 and gcd(modulus, number) == 1)
    totient_memo[modulus] = totient
    return totient

def order(number, modulus):
    current_value = number
    exponent = 1
    for _ in range(0, euler_totient(modulus)):
        if current_value == 0 or current_value == 1:
            return exponent
        current_value = current_value * number % modulus
        exponent += 1

def is_primitive_root(number, modulus):
    return order(number, modulus) == euler_totient(modulus)

def find_primitive_roots(modulus):
    return (number for number in range(modulus) if is_primitive_root(number, modulus))

def find_orders(modulus):
    return (order(number, modulus) for number in range(modulus))
