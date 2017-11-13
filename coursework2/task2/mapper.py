#!/usr/bin/python

import sys
import heapq
import xml.etree.ElementTree as Etree

heap = []

for line in sys.stdin:
    if line.strip()== "": 
        continue
    try:
        tree_XML = Etree.fromstring(line.strip())
        str_type = tree_XML.attrib["PostTypeId"]
    except BaseException:
        continue
    if str_type == "1":
        str_cnt = tree_XML.attrib["ViewCount"]
        str_id = tree_XML.attrib["Id"]
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
    print "%d\t%s"%(item[0],item[1])
    
