def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


# A bottom-up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    print(bottom_up)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]


if __name__ == '__main__':
    print(fib_bottom_up(5))
