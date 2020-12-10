#!/home/cloudera/miniconda3/bin/python3.8
import sys
import csv

data = sys.stdin.readlines()
for line in csv.reader(data, delimiter='|'):
    #print("yayayay"+line[0])
    #print(line)
    print('%s    %s' % (line[2], line[4]))