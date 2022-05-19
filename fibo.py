def fib(n):
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a,b = b,a+b
    print()


def fib2(s):
    result = []
    a,b = 0,1
    while b < s:
        result.append(b)
        a,b = b,a+b
    print(result)

