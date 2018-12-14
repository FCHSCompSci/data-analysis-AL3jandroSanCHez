import csv

filename = 'boxoffice.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        mcu_movies = []
        if reader[2] == 'BV':
            mcu_movies.append(reader[1])




    for row in reader:
        print(f'{row[3]}: year: {row[4]}')


