from __future__ import print_function, division


def max_overlapping(intervals):
    """
    notice that the minimum number of classroom halls is the maximum number of overlapping intervals.
    """
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)

    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1
    return current_max


if __name__ == "__main__":
    array = [(30, 75), (0, 50), (60, 150)]
    assert max_overlapping(array) == 2
