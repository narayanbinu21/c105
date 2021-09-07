import math
import csv

with open('data.csv', newline='') as f:
   reader = csv.reader(f)
   file_date = list(reader)

data = file_date[0]

def mean(data):
    n =len(data)
    total =0
    for x in data:
        total+= int(x)
    mean = total /n
    return mean 