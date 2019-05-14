
from random import random
from math import hypot


def monteCarloApprox(trials):
    """
    Create random x and y coordinates in 1000000 trials
    For each time the euclidian distance between x and y is less than 1 (it means it is inside the circle) and we add 1
    PI is close to 4 times the result of the division between the nr of times the euclidian distance was inside the circle and the nr of total trials

    The Area of a circle is πr^2. If we set r to be less than 1 and positive, then we can more easily approximate pi
    """
    inside = 0
    for i in range(trials):
        x = random()
        y = random()
        if hypot(x, y) < 1:
            inside += 1
    print('I think pi is: ', 4.0 * inside / trials, inside)


if __name__ == '__main__':
    trials = 10 ** 6
    monteCarloApprox(trials)
