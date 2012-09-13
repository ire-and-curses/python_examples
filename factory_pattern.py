#!/usr/bin/env python

'''
factory_pattern.py - Example implementation of the factory pattern in Python.

The factory pattern allows dynamic creation of different objects, according to
circumstances. It also insulates the client from direct instantiation of the
dependent objects, reducing coupling between the code.

Here we use a dictionary as a dispatch table. Parser is an interface, describing the
public API of the concrete classes our Factory returns.

Concrete implementations are marked as pseudo-private using the leading
underscore notation. This means they won't be imported automatically when
doing an import *.

Author: Martin Norbury, Eric Saunders
August 2011
'''

class Factory(object):

    def __init__(self):
        self.dispatch = {
                         'xml' :_XmlParser,
                         'json':_JsonParser
                        }

    def create_parser(self, name):
        return self.dispatch.get(name, _NullParser)()


class Parser(object):
    def parse(self):
        raise NotImplementedError('This should be implemented by the subclass.')


class _XmlParser(Parser):
    def parse(self):
        print 'Parsing an xml document'


class _JsonParser(Parser):
    def parse(self):
        print 'Parsing a json document'


class _NullParser(Parser):
    pass


if __name__ == '__main__':

    factory     = Factory()
    xml_parser  = factory.create_parser('xml')
    json_parser = factory.create_parser('json')
    null_parser = factory.create_parser('wibble')

    for parser in (xml_parser, json_parser, null_parser):
        parser.parse()
