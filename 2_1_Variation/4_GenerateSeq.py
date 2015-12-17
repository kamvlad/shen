from math import factorial


def generateSeq(length):
    cur = [1] * length
    hasNext = True
    rslt  = set()

    while hasNext:
        rslt.add(tuple(cur))
        hasNext = False
        for idx in xrange(length):
            if cur[idx] < (idx + 1):
                hasNext = True
                cur[idx] += 1
                for idx2 in xrange(idx):
                    cur[idx2] = 1
                break
    return rslt

def checkSeq(n, actual):
    expectedCount = factorial(n)
    if expectedCount != len(actual):
        print 'invalid count of variations. expected =', expectedCount, ' actual =', len(actual)
        return False

    for v in actual:
        for idx in xrange(n):
            if not (1 <= v[idx] <= (idx + 1)):
                print 'invalid variation :', v
                return False

    return True

def testSeq(n):
    seqs = generateSeq(n)
    if not checkSeq(n, seqs):
        print 'Test with n =', n, 'FAILED'
        print seqs
    else:
        print 'Test with n =', n, 'PASS'

def main():
    testSeq(3)
    testSeq(5)
    testSeq(7)

if __name__ == '__main__':
    main()
