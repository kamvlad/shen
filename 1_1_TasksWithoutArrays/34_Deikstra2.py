def f(n):
    if n == 0:
        return 13
    elif n == 1:
        return 17
    elif n == 2:
        return 20
    elif n == 3:
        return 30
    elif n % 2 == 0:
        return 43 * f(n / 2) + 57 * f(n / 2 + 1)
    else:
        return 91 * f(n / 2) + 179 * f(n / 2 + 1)

# TODO not done
def fastF(n):
    if n == 0:
        return 13
    elif n == 1:
        return 17
    elif n == 2:
        return 20
    elif n == 3:
        return 30

    a = 0
    b = 0
    c = 0

    while (n > 3):
        if n % 2 == 0:
            na = 43 * a + 91 * b
            nb = 57 * a + 179 * b + 43 * c
            nc = 178 * c
        else:
            na = 91 * a
            nb = 179 * a + 43 * b + 91 * c
            nc = 179 * a + 57 * b + 179 * c

        a = na
        b = nb
        c = nc


def main():
    print f(10)

if __name__ == '__main__':
    main()