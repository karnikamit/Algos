__author__ = 'CYBORG'
# product-sum number
import time


def find_nos(n, k):
    """
    minimal product-sum number
    :param n:  range of numbers
    :param k: no of divisors
    :return: a list of numbers whose sum and product are equal
    """
    nos = {}
    main = []
    for i in range(1, n+1):
        nos[i] = []
        j = 1
        while j < i:
            if i % j == 0:
                nos[i].append(j)
            j += 1
        print(nos)
    #     if len(nos[i]) == k:
    #         s = sum(nos[i])
    #         l = 1
    #         for p in nos[i]:
    #             l *= p
    #         if l == s:
    #             main.append({i: nos[i]})
    # return main


start_time = time.time()
print(find_nos(10, 3), "- time taken", time.time()-start_time)
