#!/usr/bin/python

import sys
import heapq

heap = []

for line in sys.stdin:
    str_cnt,str_id = line.split("\t",1)
    str_cnt = str_cnt.strip()
    str_id = str_id.strip()
    if str_cnt != ""  and str_id != "":
        count = int(str_cnt)
        if len(heap) < 10:
            heapq.heappush(heap,(count,str_id))
        elif (heap[0])[0] < count:
            heapq.heappop(heap)
            heapq.heappush(heap,(count,str_id))
    else:
        continue

for item in heapq.nlargest(10,heap):
    print "%d %s"%(item[0],item[1])
