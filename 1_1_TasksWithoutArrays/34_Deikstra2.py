def f(n):
    if n == 0:
        return 13
    elif n == 1:
        return 17
    elif n == 2:
        return 20
    elif n % 2 == 0:
        return 43 * f(n / 2) + 57 * f(n / 2 + 1)
    else:
        return 91 * f(n / 2) + 179 * f(n / 2 + 1)

def fastF(n):
    if n == 0:
        return 13

    # f_n = a * f_n + b * f_n+1 + c * f_n+2

    a = 1
    b = 0
    c = 0

    while (n > 2):
        # n = 2k => f_n = (43 * a + 91 * b) * f_n + (57 * a + 179 * b + 43 * c) * f_n+1 + 57 * c * f_n+2
        if n % 2 == 0:
            na = 43 * a + 91 * b
            nb = 57 * a + 179 * b + 43 * c
            nc = 57 * c
        # n = 2k + 1 => f_n = (91 * a) * f_n + (179 * a + 43 * b + 91 * c) * f_n+1 + (57 * b + 179 * c) * f_n+2
        else:
            na = 91 * a
            nb = 179 * a + 43 * b + 91 * c
            nc = 57 * b + 179 * c

        a = na
        b = nb
        c = nc

        # n = k
        n = n / 2

    # f_2 = (91 * a) * f_1 + (a + 179 * b + 43 * c) * f_2 + (57 * c) * f_3
    if n == 2:
        na = 91 * b
        nb = a + 179 * b + 43 * c
        nc = 57 * c
        a = na
        b = nb
        c = nc

    # f_1 = (a + 91 * c) * f_1 + (b + 179 * c) * f_2
    return (a + 91 * c) * 17 + (b + 179 * c) * 20


def main():
    print f(1)
    print fastF(1)

if __name__ == '__main__':
    main()