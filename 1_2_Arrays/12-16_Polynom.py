# TODO 1.2.14 not done

# 1.2.12
def poly(a, x):
    n = len(a) - 1
    r = a[n]
    n -= 1

    while n >= 0:
        r = a[n] + x * r
        n -= 1

    return r

# 1.2.13
def polyWithDerivate(a, x):
    n = len(a) - 1
    r = a[n]
    rd = 0
    n -= 1

    while n >= 0:
        rd = r + rd * x
        r = a[n] + x * r
        n -= 1

    return (r, rd)

def main():
    print polyWithDerivate([2, 5, 3], 1)


if __name__ == '__main__':
    main()
