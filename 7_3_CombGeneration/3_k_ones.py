from math import factorial


def k_ones_in_n(a, k, p):
    r = []
    if p == len(a):
        if k == 0:
            r = [tuple(a)]
        return r
    r += k_ones_in_n(a, k, p + 1)
    if k > 0:
        a[p] = 1
        r += k_ones_in_n(a, k - 1, p + 1)
        a[p] = 0
    return r

def C(N, k):
    return factorial(N) / ((factorial(k) * factorial(N-k)))

N = 5
k = 0
rslt = (k_ones_in_n([0] * N, k, 0))
for s in rslt:
    assert (sum(s) == k)
rsltLen = len(set(rslt))
assert rsltLen == C(N, k)