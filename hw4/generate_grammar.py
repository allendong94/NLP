import math
from collections import defaultdict
from tree import Tree
def generate_grammar (f1,alpha):
    # Generate grammar
    import math
    dict_log = defaultdict(list)
    grammar_dict_nolog = defaultdict(list)
    productions_dict = defaultdict(list)
    for line in f1:
        t = Tree.from_str(line)
        for node in t.bottomup():
            if node.children == []:
                continue
            elif len(node.children) ==2 :
                #tep= ([node.children[0].label]+' '+[node.children[1].label])
                productions_dict[node.label].append([node.children[0].label+' '+node.children[1].label])
            elif node.children[0]:
                productions_dict[node.label].append([node.children[0].label] )
    max_val = 0
    max_index = 0
    max_rhs = []
    for key, value in productions_dict.iteritems():
        rule_dict = defaultdict(int)
        length = len(value)
        for v in value:
            rule_dict[str(v)] += 1
        # lidstone smoothing method
        for v in value:
            rule_dict[str(v)] += alpha
        length += length * alpha
        for k, v in rule_dict.iteritems():
            if v >max_val:
                max_val = v
                max_index = key
                max_rhs = k[2:-2]
            probability = (float(v) / float(length))
            grammar_dict_nolog[key].append([k[2:-2], probability])
            prob_log = math.log(float(v) / float(length), 10)
            dict_log[key].append([k[2:-2], prob_log])
    # Write to grammar.txt
    '''
    print("The most common rule is:" +str(max_index)+" -> "+str(max_rhs))
    print("The number of most common rule is:"+str(max_val))

    f = open('grammar.txt', 'w')
    for key, value in grammar_dict_nolog.iteritems():
        for v in value:
            f.write(str(key) + " -> " + str(v[0]) + " # " + str(v[1]) + "\n")
    f.close()
    '''
    return dict_log