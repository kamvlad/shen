def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return f(n / 2)
    else:
        return f(n / 2) + f(n / 2 + 1)

def fastF(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n % 2 == 0:
        a = 1
        b = 0
    else:
        a = 1
        b = 1
    n = n / 2

    while n != 1:
        if n % 2 == 0:
            a = a + b
        else:
            b = a + b
        n = n / 2

    return a + b

def main():
    print f(123)
    print fastF(123)


if __name__ == '__main__':
    main()
