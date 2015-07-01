__author__ = 'karnikamit'


def merge(x, y):
    """

    :param x: sorted list
    :param y: sorted list
    :return: merge both sorted list to one new list
    """
    result = []
    i = 0
    j = 0

    while True:
        if i >= len(x):          # If xs list is finished,
            result.extend(y[j:])  # Add remaining items from ys
            return result          # And we're done.

        if j >= len(y):          # Same again, but swap roles
            result.extend(x[i:])
            return result

        # Both lists still have items, copy smaller item to result.
        if x[i] <= y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1

a = range(10)
b = range(20)
print merge(a, b)
