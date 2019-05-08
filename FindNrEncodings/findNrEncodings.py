from __future__ import print_function, division

from collections import defaultdict

"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

We have a good starting point. We can see that the recursive structure is as follows:

    If string starts with zero, then there's no valid encoding.
    If the string's length is less than or equal to 1, there is only 1 encoding.
    If the first two digits form a number k that is less than or equal to 26, we can count the number of encodings assuming we pick k as a letter.
    We can also pick the first digit as a letter and count the number of encodings with this assumption.


! Interesting observation. As long there is no combination of two characters with a value higher than 26, the result will correspond to the element in the fibonacci sequence
1111 will give 5
11111 will give 8
etc.
"""


def num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)] = 1  # Empty string is 1 valid encoding

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]


if __name__ == "__main__":
    s = "111"
    print("The number of encodings should be 3 for 111. The result is:",
          num_encodings(s))
    print("111 is a + k, k + a, a + a + a")
