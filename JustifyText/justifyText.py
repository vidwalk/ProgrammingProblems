from __future__ import print_function, division
from math import floor


def min_line(words):
    return ' '.join(words)


def group_lines(words, k):
    '''
    Returns groupings of |words| whose total length, including 1 space in between,
    is less than |k|.
    '''
    groups = []
    current_sum = 0
    current_line = []
    for i, word in enumerate(words):
        # Check if adding the next word would push it over
        # the limit. If it does, then add |current_line| to
        # group. Also reset |current_line| properly.
        if len(min_line(current_line + [word])) > k:
            groups.append(current_line)
            current_line = []
        current_line.append(word)

    # Add the last line to groups.
    groups.append(current_line)
    return groups


def justify(words, length):
    '''
    Precondition: |words| can fit in |length|.
    Justifies the words using the following algorithm:
        - Find the smallest spacing between each word (available_spaces / spaces)
        - Add a leftover space one-by-one until we run out
    '''
    if len(words) == 1:
        word = words[0]
        num_spaces = length - len(word)
        spaces = ' ' * num_spaces
        return word + spaces
    spaces_to_distribute = length - sum(len(word) for word in words)
    number_of_spaces = len(words) - 1
    smallest_space = floor(spaces_to_distribute / number_of_spaces)
    leftover_spaces = spaces_to_distribute - \
        (number_of_spaces * smallest_space)
    justified_words = []
    for word in words:
        justified_words.append(word)
        current_space = ' ' * smallest_space
        if leftover_spaces > 0:
            current_space += ' '
            leftover_spaces -= 1
        justified_words.append(current_space)
    return ''.join(justified_words).rstrip()


def justify_text(words, k):
    return [justify(group, k) for group in group_lines(words, k)]


if __name__ == "__main__":
    array = ["the", "quick", "brown", "fox",
             "jumps", "over", "the", "lazy", "dog"]
    print(justify_text(array, k=16))
