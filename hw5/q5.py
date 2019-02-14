#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
###Provide your answer below
list = list()
###Answer examples; replace with your choices

list.append(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jack'],set(['jack']),distsim.cossim_dense))
list.append(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['students'],set(['students']),distsim.cossim_dense))
list.append(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['lovely'],set(['lovely']),distsim.cossim_dense))
list.append(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['fly'],set(['fly']),distsim.cossim_dense))
list.append(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['california'],set(['california']),distsim.cossim_dense))
list.append(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['vehicles'],set(['vehicles']),distsim.cossim_dense))
#for #1 and #2 similarity words of 'jack'
list.append(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['sam'],set(['sam']),distsim.cossim_dense))
list.append(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jim'],set(['jim']),distsim.cossim_dense))
f = open('q5_data','w')
print 'jack'
f.write('jack: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jack'],set(['jack']),distsim.cossim_dense), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'students'
f.write('\n'+'students: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['students'],set(['students']),distsim.cossim_dense), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'lovely'
f.write('\n'+'lovely: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['lovely'],set(['lovely']),distsim.cossim_dense), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'fly'
f.write('\n'+'fly: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['fly'],set(['fly']),distsim.cossim_dense), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'california'
f.write('\n'+'california: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['california'],set(['california']),distsim.cossim_dense), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'vehicles'
f.write('\n'+'vehicles: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['vehicles'],set(['vehicles']),distsim.cossim_dense), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'sam'
f.write('\n'+'sam: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['sam'],set(['sam']),distsim.cossim_dense), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
print 'jim'
f.write('\n'+'jim: '+'\n')
for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jim'],set(['jim']),distsim.cossim_dense), start=1):
    print("{}: {} ({})".format(i, word, score))
    f.write("{}: {} ({})".format(i, word, score))
f.close()
