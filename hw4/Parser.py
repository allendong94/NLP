from collections import defaultdict
import time
import math
from  search import search

# imply pointer data and recursively build up the parae tree
# use back-up way to construct the parse tree,  Pointer1 and Pointer2
def create_parse_tree(sentence_parse, table_parse, back_p, row, col, item):
        from tree_to_string import tree_to_str
        if back_p[row][col]:
            back_p_list = []
            temp=back_p[row][col]
            row_1 = temp[item][0][0]
            col_1 = temp[item][0][1]
            item_1 = temp[item][0][2]
            row_2 = temp[item][1][0]
            col_2 = temp[item][1][1]
            item_2 = temp[item][1][2]
            back_p_list.append(create_parse_tree(sentence_parse, table_parse, back_p, row_1, col_1, item_1))
            back_p_list.append(create_parse_tree(sentence_parse, table_parse, back_p, row_2, col_2, item_2))
        else:
            back_p_list = [sentence_parse[col - 1]]
        tree_table = table_parse[row][col][item][0]
        return str("("+str(tree_table)+" "+' '.join(back_p_list)+")")


#The CKY Parser applied viterbi algorithms, which is DP algorithm and can avoid local optimization
def parse(sentence, dict_log):
        start_time = time.time()
        # Print sentence.
        # Create the CYK table and a back pointer table
        length = len(sentence)
        table = [[ [] for col in range (length+1)] for row in range (length)]
        pointer_table=[[ [] for col in range (length+1)] for row in range (length)]
        #Fill the diagonal blanks of the CKY table. Then fill the CKY table iterally to build up the right-up blank.
        for k in range(1, length + 1):
            matched_rules = []
            for key, value in dict_log.items():
                for v in value:
                    if sentence[k - 1] == v[0]:
                        matched_rules.append([key,v[1]])

            if len(sentence[k - 1].split()) == 1 and not matched_rules:
                for key, value in dict_log.items():
                    for v in value:
                        if '<unk>' == v[0]:
                            matched_rules.append([key, v[1]])
            for termp in matched_rules:
                table[k - 1][k].extend([(termp[0], termp[1])])

        # Fill the CKY table with partial value and pointer index.
        for i in range(1, length + 1):
            for j in range(i - 2, -1, -1):
                for k in range(j + 1, i):
                    for a in range(len(table[j][k])):
                        for b in range(len(table[k][i])):
                            if time.time() - start_time > 80:
                                return None
                            root_left=table[j][k]
                            root_right=table[k][i]
                            prob = root_left[a][1] + root_right[b][1]
                            right = root_left[a][0] + ' ' + root_right[b][0]
                            matched_rules = []
                            #applied the search method to find the matching case and return
                            matched_rules = search(dict_log, matched_rules, right)
                            # x=len(word.split())
                            if len(right.split()) == 1 and not matched_rules:
                                matched_rules = search(dict_log, matched_rules, '<unk>')
                            rules_added = []
                            if len(matched_rules) is not 0:
                                for temp in matched_rules:
                                    left = [temp[0], temp[1] + prob]
                                    if left not in table[j][i]:
                                        rules_added.append(left)
                                        table[j][i].extend([left])
                                if rules_added:
                                    pointer_table[j][i].extend([[[j, k, a], [k, i, b]]] * len(rules_added))

        # Call function to generate a parse tree, using maximun probability as the pitput parse and back up building the tree.
        # Also need save the maximum situation's value and key.
        if table[0][length]:
            max_prob = float("-inf")
            num = 0
            for i in range(0, len(table[0][length])):
                prob = table[0][length][i][1]
                if prob > max_prob:
                    max_prob = prob
                    num = i
            #print("The log-probability is:" + str(max_prob))
            #print("The parser 's output's log-probability is: "+max_prob)
            #Then call method create_parse_tree recursively  to build up back-up poitners and the parse tree
            return create_parse_tree(sentence, table, pointer_table, 0, length, num)
        else:
            return None
