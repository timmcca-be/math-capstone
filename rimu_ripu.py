def rimu(a, b, k = 2):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    return rimu(a ^ b, {k * x for x in a & b}, k)

def ripu(a, b, k = 2):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    return rimu(a ^ b, {x ** k for x in a & b}, k)
