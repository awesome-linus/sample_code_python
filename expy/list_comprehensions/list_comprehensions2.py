# -*- coding: utf-8 -*-

i = 0
seq = ["one", "two", "three"]

for i, element in enumerate(seq):
    seq[i] = '%d: %s' % (i, element)


print(seq)
