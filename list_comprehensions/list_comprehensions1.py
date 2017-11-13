# -*- coding: utf-8 -*-

size = 10
arrays = []
i = 0

[arrays.append(i) for i in range(size) if i % 2 == 0 and i != 4]

print(arrays)
