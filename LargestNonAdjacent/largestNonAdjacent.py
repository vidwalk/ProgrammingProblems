from __future__ import print_function, division

"""
we should look at this problem recursively. 
Say we had a function that already returns the largest sum of non-adjacent integers on smaller inputs. 
How could we use it to figure out what we want?
"""
def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last= max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])

    for num in arr[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)

if __name__ == "__main__":
    lst = [2, 4, 6, 2, 5]
    print("It should return 13, and it returns", largest_non_adjacent(lst), "for [2, 4, 6, 2, 5]")