#!/home/cloudera/miniconda3/bin/python3.8
import sys
dict={}

for line in sys.stdin:
    line = line.strip()
    store, count = line.split('    ')
    count = int(count)
    
    if (store + "_max") in dict and (store + "_min") in dict:
        if dict[store + "_max"] < int(count):
            dict[store + "_max"] = int(count)
        if dict[store + "_min"] > int(count):
            dict[store + "_min"] = int(count)
    else:
        dict[store + "_max"]=int(count)
        dict[store + "_min"]=int(count)
        	
for key in dict:
    print('%s    %s'    % (key,dict[key]))
