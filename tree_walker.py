#!/usr/bin/env python

'''
tree_walker.py - Functional programming implementation of a tree walking algorithm.

Simple example of a general recursive tree-walking function.

Author: Eric Saunders
June 2012
'''


def is_a_node(node):
    if isinstance(node, tuple):
        return True

    return False

def get_children(node):
    return node


node_total = 0
def process_node(node):
    global node_total
    print "Found a node:", node
    node_total += 1


leaf_total = 0
def process_leaf(node):
    global leaf_total
    print "Found a leaf:", node
    leaf_total += 1



def walk(node, is_a_node, get_children, process_node, process_leaf ):

        if is_a_node(node):
            process_node(node)
            for child in get_children(node):
                walk(child, is_a_node, get_children, process_node, process_leaf)

        else:
            process_leaf(node)
            return


if __name__ == '__main__':

    tree = (
                ( 1, 2 ),
                ( 3, ),
                (
                    ( 4, 5 ),
                )
           )

    walk(tree, is_a_node, get_children, process_node, process_leaf)

    print "Found %d nodes." % node_total
    print "Found %d leaves." % leaf_total
