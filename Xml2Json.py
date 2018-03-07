#!/usr/bin/env python
""" Extract Certain Data from an Xml and have it create a metadata.json file of each XML file found
"""
import os
# from json import simplejson
# import xml.etree.ElementTree as ET

path = os.sys.argv[1]


def count_xmls():
    xml_count = 0
    xml_list = []
    print ("..............This count All XML files that have been obtained from the path")
    for r, d, files in os.walk(path):
        for f in files:
            if f.endswith('.XML'):
                print f
                xml_list.append(f)
                xml_count += 1
            # for f in xml_list:
    print "Total XML Files are : %d" % xml_count


if __name__ == '__main__':
    count_xmls()
