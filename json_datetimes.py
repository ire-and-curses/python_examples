#!/usr/bin/env python

'''
json_datetimes.py - Allow json to handle datetime serialisation transparently

description

Author: Eric Saunders
September 2012
'''

import json
from datetime import datetime

dt_handler1 = lambda obj: obj.isoformat() if isinstance(obj, datetime) else None

class hello(object):
    def __init__(self, **kwargs):
        pass

    def encode(self, obj):
        print obj
        return "hello!"




def dt_handler2(obj):
    print "Entered dt_handler2"
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()


data_structure = { 'a' : 4, 'b' : 'herring', 'c': datetime.now(), 'd':json }

#print json.dumps(data_structure, default=dt_handler1)
print json.dumps(data_structure, cls=hello)
#print json.dumps(data_structure)
