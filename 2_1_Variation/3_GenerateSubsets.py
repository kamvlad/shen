def generateVariations(n, length):
    cur = [1] * length
    hasNext = True
    rslt  = set()

    while hasNext:
        rslt.add(tuple(cur))
        hasNext = False
        for idx in xrange(length):
            if cur[idx] < n:
                hasNext = True
                cur[idx] += 1
                for idx2 in xrange(idx):
                    cur[idx2] = 1
                break
    return rslt

def generateSubset(k):
    variations = generateVariations(2, k)

    rslt = set()
    for v in variations:
        cur = []
        for idx in xrange(k):
            if v[idx] == 2:
                cur += [idx + 1]
        rslt.add(tuple(cur))
    return rslt

def checkSubsets(k, subsets):
    if len(subsets) != 2 ** k:
        print 'invalid count of variations. expected =', 2 ** k, ' actual =', len(subsets)
        return False
    return True

def testSubsets(k):
    subsets = generateSubset(k)
    if not checkSubsets(k, subsets):
        print 'Test with k =', k, 'FAILED'
        print subsets
    else:
        print 'Test with k =', k, 'PASS'


def main():
    testSubsets(3)
    testSubsets(10)
    testSubsets(1)

if __name__ == '__main__':
    main()
