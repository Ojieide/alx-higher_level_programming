#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """
    size = len(list_of_integers)
    m1 = size
    m2 = size // 2

    if size == 0:
        return None

    while True:
        m1 = m1 // 2
        if (m2 < size - 1 and
                list_of_integers[m2] < list_of_integers[m2 + 1]):
            if m1 // 2 == 0:
                m1 = 2
            m2 = m2 + m1 // 2
        elif m1 > 0 and list_of_integers[m2] < list_of_integers[m2 - 1]:
            if m1 // 2 == 0:
                m1 = 2
            m2 = m2 - m1 // 2
        else:
            return list_of_integers[m2]
