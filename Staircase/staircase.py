from __future__ import print_function, division

"""
The only ways to get to N = 3, is to first get to N = 1, and then go up by 2 steps, or get to N = 2 and go up by 1 step. So f(3) = f(2) + f(1).

Does this hold for N = 4? Yes, it does. Since we can only get to the 4th step by getting to the 3rd step and going up by one, or by getting to the 2nd step and going up by two. So f(4) = f(3) + f(2).

To generalize, f(n) = f(n - 1) + f(n - 2). That's just the Fibonacci sequence!
"""


def staircase(n, X):
    """
    Parameters

    n - steps

    X - set with how many steps can be climbed ex {1,3,5} means how many ways to climb n steps if you can climb 1 step at a time, 3 steps at a time or 5 steps at a time

    """
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]


if __name__ == "__main__":
    X = {1, 2}
    print('if N is 4, and you can climb up either 1 or 2 steps at a time then there are',
          staircase(4, X), 'ways to do it')
