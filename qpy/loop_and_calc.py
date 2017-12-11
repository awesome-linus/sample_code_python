calc_result = {}
name_lunch = {}

# open 'data_sample/name_gender.csv' and calculate
with open('data_sample/name_gender.csv') as f:
    for row in f:
        strip_row = row.rstrip()
        row_item = strip_row.split(',')
        name = row_item[0]
        gender = row_item[1]

        if gender not in calc_result:
            calc_result[gender] = 1
        else:
            calc_result[gender] += 1

# display

for menu_name, count in calc_result.items():
    print(menu_name + ':' + str(count))
