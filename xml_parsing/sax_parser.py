#!/usr/bin/env python

import sys
from xml.sax import make_parser, handler


class PrintContentsHandler(handler.ContentHandler):

    def startElement(self, name, attrs):
        '''Called whenever a new element is encountered.'''

        print "Starting element: ", name

        for aname in attrs.getNames():
            print "    attribute: %s = %s" % (aname, attrs.getValue(aname))


    def endElement(self, name):
        '''Called when the end of an element is reached.'''

        print "Ending element: ", name


    def characters(self, data):
        '''Called whenever there is raw data available.'''

        print "Found characters:", data



class SEMSHandler(handler.ContentHandler):

    def __init__(self):
        self.dictionary = {}
        handler.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        '''Called whenever a new element is encountered.'''

        print "Starting element: ", name

        self.current_element = name


    def endElement(self, name):
        '''Called when the end of an element is reached.'''

        print "Ending element: ", name


    def characters(self, data):
        '''Called whenever there is raw data available.'''

        print "Found characters:", data

        self.dictionary[self.current_element] = data



xml_file_to_read = 'output.xml'
if len(sys.argv) > 1:
    xml_file_to_read = sys.argv[1]

p = make_parser()
handler = SEMSHandler()
p.setContentHandler(handler)
p.parse(xml_file_to_read)

contents = handler.dictionary



for key in contents:
    print key, contents[key]

