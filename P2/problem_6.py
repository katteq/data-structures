import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_e = None
    max_e = None

    for element in ints:
        if max_e == None or element > max_e:
            max_e = element
        if min_e == None or element < min_e:
            min_e = element
    return (min_e, max_e)


def test(min_range, max_range, expected):
    l = [i for i in range(min_range, max_range)]
    random.shuffle(l)

    actual = get_min_max(l)
    print("Pass" if (expected == actual) else "Fail")


test(0, 10, (0, 9))
test(-90, 20, (-90, 19))
test(-1, 2, (-1, 1))
