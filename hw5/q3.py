#!/usr/bin/env python
import distsim

word_to_ccdict = distsim.load_contexts("nytcounts.4k")


### provide your answer below

list = list()
###Answer examples; replace with your choices

list.append(distsim.show_nearest(word_to_ccdict, word_to_ccdict['jack'],set(['jack']),distsim.cossim_sparse))
list.append(distsim.show_nearest(word_to_ccdict, word_to_ccdict['students'],set(['students']),distsim.cossim_sparse))
list.append(distsim.show_nearest(word_to_ccdict, word_to_ccdict['lovely'],set(['lovely']),distsim.cossim_sparse))
list.append(distsim.show_nearest(word_to_ccdict, word_to_ccdict['fly'],set(['fly']),distsim.cossim_sparse))
list.append(distsim.show_nearest(word_to_ccdict, word_to_ccdict['california'],set(['california']),distsim.cossim_sparse))
list.append(distsim.show_nearest(word_to_ccdict, word_to_ccdict['vehicles'],set(['vehicles']),distsim.cossim_sparse))
#for #1 and #2 similarity words of 'jack'
list.append(distsim.show_nearest(word_to_ccdict, word_to_ccdict['adam'],set(['adam']),distsim.cossim_sparse))
list.append(distsim.show_nearest(word_to_ccdict, word_to_ccdict['james'],set(['james']),distsim.cossim_sparse))
f = open('q3_data','w')
print 'jack'
f.write('jack: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['jack'],set(['jack']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'students'
f.write('\n'+'students: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['students'],set(['students']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'lovely'
f.write('\n'+'lovely: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['lovely'],set(['lovely']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'fly'
f.write('\n'+'fly: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['fly'],set(['fly']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'california'
f.write('\n'+'california: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['california'],set(['california']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'vehicles'
f.write('\n'+'vehicles: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['vehicles'],set(['vehicles']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'adam'
f.write('\n'+'adam: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['adam'],set(['adam']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'james'
f.write('\n'+'james: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict['james'],set(['james']),distsim.cossim_sparse), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
f.close()
