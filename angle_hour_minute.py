"""
WAP to find the angle between Hour and minute hands in an analog clock.
"""
import math


def angle(hour, minute):
    """

    :param (int) hour:
    :param (int) minute:
    :return (int): angle between hour and minute hands
    """
    # hour hand moves at the rate of 0.5 degrees per minute
    # minute hand moves at the rate of of 6 degrees per minute
    hour_angle = 0.5 * (hour * 60) + minute
    minute_angle = 6 * minute
    hm_angle = math.fabs(hour_angle - minute_angle)
    return min(hm_angle, 360-hm_angle)


if __name__ == '__main__':
    print angle(10, 55)
