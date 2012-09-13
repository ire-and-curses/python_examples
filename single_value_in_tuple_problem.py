#!/usr/bin/python

#Example 1
def scalar_or_list(scalar=True):
   if scalar:
       return ("a single string")
   else:
       return ('aa','bb','cc')

#print "Calling function to return single value tuple..."
#for value in scalar_or_list():
#   print "Value was:", value


#print "Calling function to return multiple value tuple..."
#for value in scalar_or_list(scalar=False):
#   print "Value was:", value




#Example 2
    def tuple_maker(values):
        my_tuple = (values)
        return my_tuple


    for val in tuple_maker("a single string"):
        print "Value was", val

    for val in tuple_maker(["str1", "str2", "str3"]):
        print "Value was", val
