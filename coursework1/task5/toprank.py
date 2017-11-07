#!/usr/bin/python

import sys
import heapq

heap = []

for line in sys.stdin:
    tokens,scount = line.split("\t",1)
    count = int(scount)
    if len(heap) < 25:
        heapq.heappush(heap,(count,tokens))
    elif (heap[0])[0] < count:
        heapq.heappop(heap)
        heapq.heappush(heap,(count,tokens))
    else:
        continue
if len(sys.argv) > 1:
    if sys.argv[1] == "mapper":
        for item in heapq.nlargest(25,heap):
            print "%s\t%d"%(item[1],item[0])
    elif sys.argv[1] == "reducer":
        for item in heapq.nlargest(25,heap):
            print "%d\t%s"%(item[0],item[1])

    
   
