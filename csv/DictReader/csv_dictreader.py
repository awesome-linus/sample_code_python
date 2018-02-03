# -*- coding: utf-8 -*-

import csv

csv_header = ['名前', '名前フリガナ', '性別', '血液型', '生年月日']

with open('csv_without_header.csv', 'r') as f:
    # DictReaderと共にHeaderを渡すと辞書で返してくれる。
    for row in csv.DictReader(f, csv_header):
        print(row)
