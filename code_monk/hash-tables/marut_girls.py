# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

n_Q = int(raw_input())
required_qualities = map(int, raw_input().split(' '))
assert len(required_qualities) == n_Q

no_girls = int(raw_input())
girls_qualities = {}
for _ in xrange(no_girls):
    girls_qualities[_] = map(int, raw_input().split(' '))


def select(qualities_required, girls):
    """

    :param qualities_required:
    :param girls:
    :return: No of girls selected.
    """
    selected = 0
    qualitites_set = set(qualities_required)
    temp_girls = {girl: girls.get(girl) for girl in filter(lambda x: len(girls[x]) >= len(qualities_required), girls)}
    # Usind set DS
    for g in temp_girls:
        temp_girl_qualities = set(temp_girls[g])
        if not len(temp_girl_qualities - qualitites_set):
            selected += 1
        elif temp_girl_qualities >= qualitites_set:
            selected += 1
    return selected

print select(required_qualities, girls_qualities)
