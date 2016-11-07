import csv
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)
count = 0
with open('accounds_ua.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, dialect='mydialect')
    for row in reader:
        print(row[0] + "\t \t" + row[1] + "\t \t" + row[2] + "\t \t" + row[3] + "\t \t" + row[4])
        count += 1
        print('\t \t%d' % (count%2))
