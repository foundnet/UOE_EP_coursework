#!/usr/bin/python

import sys
import xml.etree.ElementTree as Etree

for line in sys.stdin:
    if line.strip()== "": 
        continue
    try:
        tree_XML = Etree.fromstring(line.strip())
        str_type = tree_XML.attrib["PostTypeId"]
        if str_type == "1":
            str_aid = tree_XML.attrib["AcceptedAnswerId"].strip()
            str_qid = tree_XML.attrib["Id"].strip()
            if str_aid != ""  and str_qid != "":
                print str_aid + "\tQ"+str_qid
        elif str_type == "2":
            str_aid = tree_XML.attrib["Id"].strip()
            str_uid = tree_XML.attrib["OwnerUserId"].strip()
            if str_aid != "" and str_uid != "":
                print str_aid + "\tU" + str_uid
        else:
            continue
    except BaseException:
#        print "Error in:" + line
        continue
 
