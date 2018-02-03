# -*- coding: utf-8 -*-

import csv


def get_csv_dict():
    csv_header = ['名前', '名前フリガナ', '性別', '血液型', '生年月日']

    csv_dict = []
    with open('csv_without_header.csv', 'r') as f:
        # DictReaderと共にHeaderを渡すと辞書で返してくれる。
        for row in csv.DictReader(f, csv_header):
            csv_dict.append(row)
    return csv_dict


csv_dicts = get_csv_dict()

want_item_header = ['名前', '性別']
for csv_dict in csv_dicts:
    print(([csv_dict[h] for h in want_item_header]))
