#!/usr/bin/env python


def simple_fib(n):
    a = 0
    b = 1

    for i in range(n):
        c = a + b
        a = b
        b = c

    return c


def iter_fib(n):

    a, b = 0, 1

    for i in range(n-1):
        a, b = b, a+b

    return b


def fib_series(n):
    a, b, = 0, 1
    series = [0, 1]


    if n == 0:
        return [0]

    for i in range(n-1):
        a, b = b, a+b
        series.append(b)

    return series


def recursive_fib(n):
    if n in (0, 1): return n
    return recursive_fib(n-1) + recursive_fib(n-2)

stored = {
           '0' : 0,
           '1' : 1
          }

def memoized_fib1(n):
    if str(n) in stored: return n

    if str(n-1) in stored:
        a = stored[str(n-1)]
    else:
        a = memoized_fib(n-1)
        stored[str(n-1)] = a

    b = stored[str(n-2)]

    return a + b


stored = [0,1]
def memoized_fib2(n):
    if n < len(stored): return stored[n]

    if n-1 <= len(stored):
        a = stored[n-1]
    else:
        a = memoized_fib2(n-1)
        stored.insert[n-1, a]

    b = stored[n-2]

    return a + b


if __name__ == "__main__":
    n = 60
    print "n =", n
    print fib_series(n)
    #print "Simple fib:", simple_fib(n)
    print "Explicit iteration:", iter_fib(n)
    #print "Recursive fib:", recursive_fib(n)
    print "Memoized fib:", memoized_fib2(n)
