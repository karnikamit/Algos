__author__ = 'karnikamit'


# Forming a prefix table
def prefix_table(pattern):
    m = len(pattern)
    f = [0]*m
    k = 0
    for q in xrange(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = f[k-1]
        if pattern[k] == pattern[q]:
            k += 1
        f[q] = k
    return f


# Matching algorithm
def kmp(text, pattern):
    """
    complexity O(n),
    it avoids the caparisons with elements of T that were previously involved
     in comparison with some element of the pattern p.

    :param text: String to be searched
    :param pattern: pattern to be matched
    :return: index of first occurrence
    """
    n = len(text)
    m = len(pattern)
    f = prefix_table(pattern)
    q = 0
    for i in xrange(n):
        while q > 0 and pattern[q] != text[i]:
            q = f[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            return i - m + 1
    return -1

print kmp("Hello my name is Amit", "name is Amit")
