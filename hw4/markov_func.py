from tree import Tree
from tree import Node
class markov(Tree):

    def remove_unit(self):
        """ Remove unary nodes by fusing them with their parents. """
        nodes = list(self.bottomup())
        for node in nodes:
            if len(node.children) == 1:
                child = node.children[0]
                if len(child.children) > 0:
                    node.label = "%s_%s" % (node.label, child.label)
                    child.detach()
                    for grandchild in list(child.children):
                        node.append_child(grandchild)
    def binarize(self):
        """ Binarize into a left-branching or right-branching structure
        using linguistically motivated heuristics. Currently, the heuristic
        is extremely simple: SQ is right-branching, everything else is left-branching. """
        nodes = list(self.bottomup())
        for node in nodes:
            if len(node.children) > 2:
                if node.label in ['SQ']:
                    # create a right-branching structure
                    children = list(node.children)
                    children.reverse()
                    vlabel = node.label+"*"
                    prev = children[0]
                    for child in children[1:-1]:
                        prev = Node(vlabel, [child, prev])
                    node.append_child(prev)
                else:
                    # create a left-branching structure
                    vlabel = node.label+"*"
                    children = list(node.children)
                    prev = children[0]
                    for child in children[1:-1]:
                        prev = Node(vlabel, [prev, child])
                    node.insert_child(0, prev)
    def horizontal(self):
        nodes = list(self.bottomup())
        for node in nodes:
            if len(node.children) > 1:
                # for left branching
                if '*' in node.children[0].label:
                    node.children[0].label = node.children[0].label + '_' + node.children[1].label
                # for right branching
                elif '*' in node.children[1].label:
                    node.children[1].label = node.children[1].label + '_' + node.children[0].label
    def vertical(self):
        nodes = list(self.bottomup())
        for node in nodes:
            if len(node.children) > 1:
                for child in node.children:
                    if '*' in child.label:
                       child.label = node.label+'_'+child.label
