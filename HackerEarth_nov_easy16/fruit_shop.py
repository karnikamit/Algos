# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

# fruits cost
apple, bannana, pear = map(int, raw_input().split(' '))
cost = {'apple': apple, 'bannana': bannana, 'pear': pear}


# Fruits available
apples, bannanas, pears = map(int, raw_input().split(' '))
availability = {'apple': apples, 'bannana': bannanas, 'pear': pears}

# coins available
coins = 14  # int(raw_input())


def get_fruits(fruits_cost, fruits_avail, coins):
    """

    :param fruits_cost: dict = {'friut': cost...}
    :param fruits_avail: dict = {'fruit': availability count...}
    :param coins: No of coins available
    :return: max fruits
    """
    sorted_cost = sorted(fruits_cost, key=lambda x: fruits_cost[x])
    fruits_buyed = {}
    for f_cost in sorted_cost:
        i = 1
        for i in xrange(1, fruits_avail[f_cost]+1):
            temp_coins = coins
            coins -= fruits_cost[f_cost]
            if not coins > 0:
                break
            try:
                fruits_buyed[f_cost] += 1
            except KeyError:
                fruits_buyed[f_cost] = 1

        else:
            fruits_buyed[f_cost] = i
        coins = temp_coins      # ignore warning
    fruits_bought = reduce(lambda x, y: fruits_buyed[x]+fruits_buyed[y], fruits_buyed)
    return fruits_bought

print get_fruits(cost, availability, coins)
