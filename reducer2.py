#!/home/cloudera/miniconda3/bin/python3.8
import sys
dict={}

for line in sys.stdin:
    line = line.strip()
    store, count = line.split('    ')
    count = int(count)
    
    if store in dict:
        dict[store]=dict[store]+int(count)
    else:
        dict[store]=int(count)
        	
for key in dict:
    print('%s    %s'    % (key,dict[key]))
