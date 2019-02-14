#!/usr/bin/env python
from collections import defaultdict
from tree_to_string import tree_to_str
import matplotlib.pyplot as plt
from generate_grammar import generate_grammar
import math
import time
import Parser
import types
import argparse
import sys
import codecs
from rbranch import prepfile
from spec_rule import spec_rule

if sys.version_info[0] == 2:
  from itertools import izip
else:
  izip = zip
from collections import defaultdict as dd
import re
import os.path
import gzip
import tempfile
import shutil
import atexit

scriptdir = os.path.dirname(os.path.abspath(__file__))
reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')
def addonoffarg(parser, arg, dest=None, default=True, help="TODO"):
    ''' add the switches --arg and --no-arg that set parser.arg to true/false, respectively'''
    group = parser.add_mutually_exclusive_group()
    dest = arg if dest is None else dest
    group.add_argument('--%s' % arg, dest=dest, action='store_true', default=default, help=help)
    group.add_argument('--no-%s' % arg, dest=dest, action='store_false', default=default, help="See --%s" % arg)

def main():
    parser = argparse.ArgumentParser(description="trivial right-branching parser that ignores any grammar passed in",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    addonoffarg(parser, 'debug', help="debug mode", default=False)
    parser.add_argument("--infile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help="input (one sentence per line strings) file")
    parser.add_argument("--grammarfile", "-g", nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help="grammar file; ignored")
    parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                        help="output (one tree per line) file")

    try:
        args = parser.parse_args()
    except IOError as msg:
        parser.error(str(msg))

    workdir = tempfile.mkdtemp(prefix=os.path.basename(__file__), dir=os.getenv('TMPDIR', '/tmp'))

    def cleanwork():
        shutil.rmtree(workdir, ignore_errors=True)

    if args.debug:
        print(workdir)
    else:
        atexit.register(cleanwork)

    infile = prepfile(args.infile, 'r')
    outfile = prepfile(args.outfile, 'w')

    '''
    infile = open('dev.strings', 'r')
    outfile = open('dev.parses', 'w')
    '''
    #outfile = open('dev.lower.parses', 'w')
    f1 = open('train.trees.pre.unk', 'r')
    #f1 = open('train.trees.pre.lower.unk', 'r')
    running_time = []
    sequence_length = []
    #grammar_dict_log = generate_grammar(f1)
    grammar_dict_log = generate_grammar(f1, 0)
    # Call Viterbi Parser
    for line in infile:
        #temp=line.lower()
        start_time = time.time()
        words = line.split()
        #words = temp.split()
        sentence_tree = Parser.parse(words, grammar_dict_log)
        if sentence_tree is None:
            #outfile.write(str(spec_rule(words[0]))+'\n')
            outfile.write("\n")
        else:
            outfile.write(sentence_tree + "\n")
        end_time = time.time()
        sequence_length.append(math.log(len(line),10))
        running_time.append(math.log((end_time - start_time),10))
    f1.close()
    infile.close()
    outfile.close()
    #draw the log-log time-sequence_length plot
    '''
    plt.figure(1)
    plt.plot(sequence_length, running_time, 'bo')
    plt.axis([0, max(sequence_length)+0.5, 0, max(running_time)+0.5])
    plt.xlabel('Sequence Length /log')
    plt.ylabel('Parsing Time /log')
    plt.title('Q3 PLOT')
    plt.show()
            # print "Parse tree: " + str(result_tree) + "\n"
    #print('finish parsing')
    '''
if __name__ == '__main__':
  main()
