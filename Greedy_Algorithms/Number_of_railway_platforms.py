__author__ = 'karnikamit'
import numpy as np

'''
1. First sort all the arrival and departure times in an array.
2. replace arrival time by 1 and departure time by -1.
3. now take the cumulative sum and the max number gives the number of platforms least req.
'''


def arr_dep(data):
    res = dict()
    res['arrivals'] = []
    res['departures'] = []
    for i in data:
        for key in data[i]:
            if key == 'arrival':
                res['arrivals'].append(data[i][key])
            elif key == 'departure':
                res['departures'].append(data[i][key])
    return res


def get_platforms(trains):
    table = arr_dep(trains)
    arrivals = table['arrivals']
    depatures = table['departures']

    # from another table with 1 for arrivals and -1 for departuers
    arr = ['1']*len(arrivals)
    dep = ['-1']*len(depatures)
    train_arr = dict(zip(arrivals, arr))
    train_dep = dict(zip(depatures, dep))

    # Now club both the dicts
    club = dict(train_arr.items() + train_dep.items())
    timings = arrivals+depatures
    timings.sort()

    # replacing arrival and departure time by 1 and -1 respectively
    new_array = []
    for item in timings:
        if item in club:
            new_array.append(int(club[item]))

    return max(np.cumsum(new_array))


train_chart = {"A": {"arrival": 900, "departure": 930}, "B": {"arrival": 915, "departure": 1300},
               "c": {"arrival": 1030, "departure": 1100}, "D": {"arrival": 1045, "departure": 1145}}
print get_platforms(train_chart)
