# -*- coding: utf-8 -*-


def _treatment(pos, element):
    return '%d: %s' % (pos, element)


i = 0
seq = ["one", "two", "three"]

seq = [_treatment(i, ele) for i, ele in enumerate(seq)]

print(seq)
