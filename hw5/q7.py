#!/usr/bin/env python
import distsim
from collections import defaultdict

f = open('word-test.v3.txt', 'r')
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
category_list = []
category_num_dict = defaultdict(list)
for line in f:
    line = line.strip('\n')
    if line[0] == '//':
        continue
    elif line[0] == ':':
        category = line.split(' ')[1]
        category_list.append(category)
    word = line.strip().split(' ')
    if len(word) == 4 :
         word1_dict = word_to_vec_dict[word[0]]
         word2_dict = word_to_vec_dict[word[1]]
         word4_dict = word_to_vec_dict[word[3]]
         ret = distsim.show_nearest(word_to_vec_dict, word1_dict - word2_dict + word4_dict,
                                    set([word[0], word[1], word[3]]),
                                    distsim.cossim_dense)

         count = 0
         find = False
         while (count < len(ret)):
             if ret[count][0] == word[2]:
                 count += 1
                 find = True
                 break
             else:
                 count +=1
         if find == False:
             count = None
             print word
             print ret

         category_num_dict[category].append([count])
#for category, num in category_num_dict.items():
count = 0
while (count < len(category_num_dict)):
    top_1 = 0
    top_5 = 0
    top_10 = 0
    items = category_num_dict[category_list[count]]
    for item in items:
      if item[0] is not None:
        if item[0] == 1:
            top_1 += 1
        if item[0] <= 5:
            top_5 += 1
        if item[0] <= 10:
            top_10 += 1
    top_1_per  = round(float(top_1) / float(len(items)),3)
    top_5_per  = round(float(top_5) / float(len(items)),3)
    top_10_per = round(float(top_10) / float(len(items)),3)
    print category_list[count] + ": " + str(top_1_per) + " " + str(top_5_per) + " " + str(top_10_per)
    count +=1
