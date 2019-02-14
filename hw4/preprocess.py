#!/usr/bin/env python

import sys, fileinput
import tree
import markov_func
#f = open('train.trees.pre', 'w')
for line in fileinput.input():

    t = tree.Tree.from_str(line)
    # Binarize, inserting 'X*' nodes.
    t.binarize()

    # Remove unary nodes
    t.remove_unit()

    #t.vertical()

    # The tree is now strictly binary branching, so that the CFG is in Chomsky normal form.
    # Make sure that all the roots still have the same label.
    assert t.root.label == 'TOP'
    
    print t

#Lowercase
'''
f1 = open('train.trees', 'r')
f2 = open('train.trees.lower', 'w')
for line in f1:
    t = tree.Tree.from_str(line.lower())
    # Binarize, inserting 'X*' nodes.
    t.binarize()
    # Remove unary nodes
    t.remove_unit()
    assert t.root.label == 'TOP' or 'top'
    f2.write(str(t)+"\n")
f1.close()
f2.close()
'''
