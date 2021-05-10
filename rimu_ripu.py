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

# def reverse_engineer(result, b, k = 2):
#     a = set()
#     b_sorted = list(b)
#     b_sorted.sort()
#     skip_set = set()
#     for item in b_sorted:
#         while item not in result:
#             a.add(item)
#             item *= k
#         skip_set.add(item)
#     for item in result:
#         if item not in skip_set:
#             a.add(item)
#     return a

# print(reverse_engineer(rimu({1, 3, 5, 7}, {1, 2, 3, 4}), {1, 2, 3, 4}))
