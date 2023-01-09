import sys
sys.setrecursionlimit(1000000000)


def even_sum(n):
    if n % 2 != 0:
        n = even_sum(n - 1)
        return n
    elif n == 0:
        return 0
    else:
        return n + even_sum(n - 2)


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


while True:
    num = int(input("Number: "))
    print("-------------------------")
    print("Even total: ", even_sum(num))
    print("-------------------------")
    print("Factorial: ", fact(num))
    print("-------------------------")


