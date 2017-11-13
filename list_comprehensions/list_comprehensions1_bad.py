# -*- coding: utf-8 -*-

size = 10
arrays = []
i = 0

while i < size:
    if i % 2 == 0 and i != 4:
        arrays.append(i)
    i += 1

print(arrays)
