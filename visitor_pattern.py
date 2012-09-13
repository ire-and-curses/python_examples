#!/usr/bin/env python

'''
visitor_pattern.py - Example implementation of the visitor pattern

In this example, a compound object comprised of three shapes is visited by
two different visitors. The visitors expect 'name' and 'area' attributes to be
present on anything that accepts them.

The compound object 'BoxOnWheels' is the exception. It chooses not to call the
visitors on itself within its accept method, although in some cases this would
be the desired behaviour.

Author: Eric Saunders
August 2012
'''



class Element(object):

    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visit(self)



class Visitor(object):

    def __init__(self):
        pass

    def visit(self, element):
        print "Visiting %s" % type(element)



class Circle(Element):
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        self.name   = 'Circle'
        self.area   =  Circle.pi * self.radius**2


class Square(Element):

    def __init__(self, edge):
        self.edge = edge
        self.name = 'Square'
        self.area = self.edge**2


class BoxOnWheels(Element):
    '''A box on wheels is a container object, made up of a square, sitting on
       top of two circles.'''


    def __init__(self, wheel_radius, box_height):
        self.wheels = [ Circle(wheel_radius), Circle(wheel_radius) ]
        self.box    = Square(box_height)


    def accept(self, visitor):
        [wheel.accept(visitor) for wheel in self.wheels]
        self.box.accept(visitor)



class AreaPrinter(Visitor):
    '''Example of a Visitor that performs an operation in a streamlike manner.'''

    def __init__(self):
        pass

    def visit(self, element):
        print "Area of the %s is %s" % ( element.name, element.area )



class AreaSummation(Visitor):
    '''Example of a Visitor that keeps a running total.'''

    def __init__(self):
        self.total_area = 0

    def visit(self, element):
        self.total_area += element.area

    def print_total_area(self):
        print "Total area of all objects was", self.total_area



if __name__ == '__main__':
    # Visitors that print and sum areas, respectively
    ap   = AreaPrinter()
    asum = AreaSummation()

    # Create our compound Element object
    box_on_wheels = BoxOnWheels(wheel_radius=2, box_height=4)

    # Visit the Element with each Visitor
    box_on_wheels.accept(ap)
    box_on_wheels.accept(asum)

    asum.print_total_area()
