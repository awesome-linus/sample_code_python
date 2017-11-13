# -*- coding: utf-8 -*-

i = 0
seq = ["one", "two", "three"]

for element in seq:
    seq[i] = '%d: %s' % (i, element)
    i += 1

print(seq)
