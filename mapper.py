#!/home/cloudera/miniconda3/bin/python3.8
import sys

for line in sys.stdin:
    #line =  line.strip()
    words = line.split()
    for word in words:
        print('%s    %s' % (word,1))
