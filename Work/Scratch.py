
import urllib.request
from xml.etree.ElementTree import parse

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)



with open('Work/Data/portfolio.csv', 'rt') as f:
    data = f.read()

with open('Work/Data/portfolio.csv', 'rt') as f:
    for line in f:
        print(line, end='')

print(data)


import csv

with open('Work/Data/portfolio.csv') as f:
    rows = csv.reader(f)
    
    for row in rows:
        print(row)


from pprint import pprint


records = []  # Initial empty list

with open('Work/Data/portfolio.csv', 'rt') as f:
    next(f) # Skip header
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))


pprint(records)

