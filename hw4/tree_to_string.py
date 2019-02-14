def tree_to_str(tree):
    # Convert parse tree to string
    length = len(tree)
    for i in range(length):
        if isinstance(tree[i], list):
            tree[i] = tree_to_str(tree[i])
    str_tree = '(' + ' '.join(tree) + ')'
    return str_tree