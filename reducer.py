#!/home/cloudera/miniconda3/bin/python3.8
import sys
dict={}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('    ',1)
    count = int(count)
    
    if word in dict:
        dict[word]=dict[word]+int(count)
    else:
        dict[word]=int(count)
        	
for key in dict:
    print('%s    %s'    % (key,dict[key]))
