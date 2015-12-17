
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

def checkVariations(n, length, actual):
    if (n ** length) != len(actual):
        print 'invalid count of variations. expected =', n ** length, ' actual =', len(actual)
        return False

    for v in actual:
        for e in v:
            if not (1 <= e <= n):
                print 'invalid variation :', v
                return False

    return True

def testVariation(n, length):
    variations = generateVariations(n, length)
    if not checkVariations(n, length, variations):
        print 'Test with n =', n, ' length=', length, 'FAILED'
        print variations
    else:
        print 'Test with n =', n, ' length=', length, 'PASS'

def main():
    testVariation(2, 10)
    testVariation(9, 5)
    testVariation(6, 1)

if __name__ == '__main__':
    main()
