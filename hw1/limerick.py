#!/usr/bin/env python
import argparse
import sys
import codecs
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

# Use word_tokenize to split raw text into words
from string import punctuation

import nltk
from nltk.tokenize import word_tokenize



scriptdir = os.path.dirname(os.path.abspath(__file__))


reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')


def prepfile(fh, code):
  if type(fh) is str:
    fh = open(fh, code)
  ret = gzip.open(fh.name, code if code.endswith("t") else code+"t") if fh.name.endswith(".gz") else fh
  if sys.version_info[0] == 2:
    if code.startswith('r'):
      ret = reader(fh)
    elif code.startswith('w'):
      ret = writer(fh)
    else:
      sys.stderr.write("I didn't understand code "+code+"\n")
      sys.exit(1)
  return ret

def addonoffarg(parser, arg, dest=None, default=True, help="TODO"):
  ''' add the switches --arg and --no-arg that set parser.arg to true/false, respectively'''
  group = parser.add_mutually_exclusive_group()
  dest = arg if dest is None else dest
  group.add_argument('--%s' % arg, dest=dest, action='store_true', default=default, help=help)
  group.add_argument('--no-%s' % arg, dest=dest, action='store_false', default=default, help="See --%s" % arg)



class LimerickDetector:

    def __init__(self):
        """
        Initializes the object to have a pronunciation dictionary available
        """
        self._pronunciations = nltk.corpus.cmudict.dict()


    def num_syllables(self, word):
        """
        Returns the number of syllables in a word.  If there's more than one
        pronunciation, take the shorter one.  If there is no entry in the
        dictionary, return 1.
        """
        # TODO: provide an implementation!
        pronunces=self._pronunciations.get(word.lower())
        if (pronunces == None):
            return 1
        '''use the available dictionary to make prnounce, use default value=1 if can not find 
        '''
        count=sys.maxint
        for pronunce in pronunces:
            temp=0;
            for phoneme in pronunce:
                if(phoneme[-1].isdigit()):
                    temp+=1
            if(count>temp):
                count=temp
        return count

    def rhymes(self, a, b):
        """
        Returns True if two words (represented as lower-case strings) rhyme,
        False otherwise.
        """
        # TODO: provide an implementation!
        key = False
        pronunces_a = self._pronunciations.get(a.lower())
        pronunces_b = self._pronunciations.get(b.lower())
        if (pronunces_a == None or pronunces_b == None):
            return key
        # announce del_consonant_b & a is 'list'

        del_consonant_a = []
        for pronunce_a in pronunces_a:
            '''
            for i in range(pronunce_a):
                if(pronunce_a[0][-1].isdigit()):
                    del_consonant_a.append(pronunce_a)
                    break
                else:
                    del pronunce_a[0]
            '''
            while (not pronunce_a[0][-1].isdigit()):
                del pronunce_a[0]

            del_consonant_a.append(pronunce_a)# del_consonant is a list of pronounciations
        del_consonant_b = []
        for pronunce_b in pronunces_b:
            '''
            for i in range(pronunce_b):
                if (pronunce_b[0][-1].isdigit()):
                    del_consonant_b.append(pronunce_b)
                    break
                else:
                    del pronunce_b[0]
            '''
            while (not pronunce_b[0][-1].isdigit()):
                del pronunce_b[0]

            del_consonant_b.append(pronunce_b)  # del_consonant is a list of pronounciations

        for del_a in del_consonant_a:  # del_ is a pronounciation
            for del_b in del_consonant_b:
                if (len(del_b) > len(del_a)):
                    short_word = list(del_a)
                    long_word = list(del_b)
                else:
                    short_word = list(del_b)
                    long_word = list(del_a)
                # for i in range (len(short_word)):
                while (short_word):
                    if (long_word[-1] != short_word[-1]):
                        break
                    else:
                        del long_word[-1]
                        del short_word[-1]
                if (len(short_word)==0):
                    key = True
                    break
            if (key):
                break
        return key

    def is_limerick(self, text):
        """
        Takes text where lines are separated by newline characters.  Returns
        True if the text is a limerick, False otherwise.

        A limerick is defined as a poem with the form AABBA, where the A lines
        rhyme with each other, the B lines rhyme with each other, and the A lines do not
        rhyme with the B lines.


        Additionally, the following syllable constraints should be observed:
          * No two A lines should differ in their number of syllables by more than two.
          * The B lines should differ in their number of syllables by no more than two.
          * Each of the B lines should have fewer syllables than each of the A lines.
          * No line should have fewer than 4 syllables

        (English professors may disagree with this definition, but that's what
        we're using here.)


        """
        # TODO: provide an implementation!
        #AABBA
        sents=[]
        for sent in text.splitlines():
            sents.append(sent)
        sent_tokenize=[]
        for sent in sents:
            if (word_tokenize(sent)!=[]):
                sent_tokenize.append(word_tokenize(sent))
        for i in range(len(sent_tokenize)):#pronunciation
            j =0
            while(j<len(sent_tokenize[i])):
              if(not all(char in punctuation for char in sent_tokenize[i][j])):
                  j+=1
              else:
                 del sent_tokenize[i][j]
                 j=j-1
        if (len(sent_tokenize) != 5):
            return False
        lastword=[]
        for i in range(len(sent_tokenize)):
            lastword.append(sent_tokenize[i][-1])
            #AABBA
        syllable_count=[0,0,0,0,0]
        for i in range(0,5):
            for word in sent_tokenize[i]:
                syllable_count[i]+=self.num_syllables( word)
            if(syllable_count[i]<4):
                return False
        if(abs(syllable_count[2]-syllable_count[3])<=2 and abs(syllable_count[0]-syllable_count[1])<=2 and abs(syllable_count[0]-syllable_count[4])<=2 and abs(syllable_count[1]-syllable_count[4])<=2):
            if(self.rhymes(lastword[0], lastword[1])and self.rhymes(lastword[0], lastword[4])and self.rhymes(lastword[4], lastword[1])and self.rhymes(lastword[2], lastword[3])):
                 return True
        return False
    # TODO: if implementing guess_syllables add that function here by uncommenting the stub code and
    # completing the function. If you want guess_syllables to be used by num_syllables, feel free to integrate it appropriately.
    #
    # def guess_syllables(self, word):
    #   """
    #   Guesses the number of syllables in a word. Extra credit function.
    #   """
    #   # TODO: provide an implementation!
    #   pass

    # TODO: if composing your own limerick, put it here and uncomment this function. is_limerick(my_limerick()) should be True
    #
    #
    # def my_limerick(self):
    #   """
    #   A limerick I wrote about computational linguistics
    #   """
    #   limerick="""
    #     Replace these words
    #     with your limerick
    #     and then test it out
    #   """
    #   return limerick


# The code below should not need to be modified
def main():
  parser = argparse.ArgumentParser(description="limerick detector. Given a file containing a poem, indicate whether that poem is a limerick or not",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  addonoffarg(parser, 'debug', help="debug mode", default=False)
  parser.add_argument("--infile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input file")
  parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output file")




  try:
    args = parser.parse_args()
  except IOError as msg:
    parser.error(str(msg))

  infile = prepfile(args.infile, 'r')
  outfile = prepfile(args.outfile, 'w')

  ld = LimerickDetector()
  lines = ''.join(infile.readlines())
  outfile.write("{}\n-----------\n{}\n".format(lines.strip(), ld.is_limerick(lines)))

if __name__ == '__main__':
  main()