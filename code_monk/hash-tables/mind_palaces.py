# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

N, M = map(int, raw_input().split(' '))
memory_hash = {}
for _ in xrange(N):
    memory_hash.setdefault(_, []).extend(map(int, raw_input().split(' ')))


def search_memory(hash_memory, memory):
    """

    :param hash_memory: a Memory dict
    :param memory: memory whose position in the matrix has to be returned
    :return: position of the memory in the matrix else -1 -1
    """
    for key in hash_memory:
        try:
            memory_index = hash_memory[key].index(memory)
            return key, memory_index
        except ValueError:
            pass
    else:
        return -1, -1


Q = int(raw_input())
for _ in xrange(Q):
    q = int(raw_input())
    a, b = search_memory(memory_hash, q)
    print '{} {}'.format(a, b)
# TODO Time Limit Exceeded - optimize the code
