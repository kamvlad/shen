import copy


def findCandidate(a, p):
    for i in range(len(a) - 1, p - 1, -1):
        if a[i] > a[p]:
            return i
    return p

def reverse(a, p):
    n = len(a) - 1
    e = (len(a) - p) >> 1

    for i in range(e):
        a[p + i], a[n - i] = a[n - i], a[p + i]

def permutate(a, p):
    if p == len(a) - 1:
        return [tuple(a)]
    r = permutate(a, p + 1)
    k = findCandidate(a, p)
    while k != p:
        a[p], a[k] = a[k], a[p]
        reverse(a, p + 1)
        r += permutate(a, p + 1)
        k = findCandidate(a, p)
    return r

# TODO implement from book

r = set(permutate(list(range(7)), 0))
print(r)
print(len(r))