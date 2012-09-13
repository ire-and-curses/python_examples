#!/usr/bin/env python

from xml.dom import minidom

sems_doc = minidom.parse('newest.xml')




def extract_data(target):

    data_dict = {}

    for value in target.childNodes:
        if value.localName == 'boltwood':
            continue

        print "localName:", value.localName
        print "nodeType:", value.nodeType


        # If it has a Text child...
        if value.nodeType == 1:
            for text in value.childNodes:
                print "contents:", text.nodeValue
                data_dict[value.localName] = text.nodeValue

    return data_dict





values = sems_doc.getElementsByTagName("values")
values_element = values[0]
values_dict = extract_data(values_element)


boltwoods = sems_doc.getElementsByTagName("boltwood")
bolt0_dict = extract_data(boltwoods[0])
bolt1_dict = extract_data(boltwoods[1])
bolt2_dict = extract_data(boltwoods[2])

bolt_list = [bolt0_dict, bolt1_dict, bolt2_dict]


status = sems_doc.getElementsByTagName("status")
status_dict = extract_data(status[0])

thresholds = sems_doc.getElementsByTagName("thresholds")
thresh_dict = extract_data(thresholds[0])
