from __future__ import print_function, division


def cons(a, b):
    """
    Python function objects are first class objects. A def statement results in a new function object, and you can retrieve that object by using the function name

    The next item to understand are closures; closures are an extra namespace attached to function objects, for variables from a surrounding scope.

    So nested functions can have access to names from the surrounding scope via closures. (Side note: it's not the value that's stored in a closure, it's the variable. 
    The variable can change over time, and just like other variables accessing the name later will reflect the new value)
    """
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def return_first(a, b):
        return a
    return pair(return_first)


def cdr(pair):
    def return_last(a, b):
        return b
    return pair(return_last)

# a clearer example


def add(first, second):
    return first + second


if __name__ == "__main__":
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))
    # Showcase how it works with others functions
    pair_test = cons(3, 4)
    pair_test(print)
    print("The sum of the cons parameters:", pair_test(add))
