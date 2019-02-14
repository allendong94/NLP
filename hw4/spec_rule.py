def spec_rule(word):
    if word =='What':
        return str("(TOP (SBARQ (WHNP (WDT What))) (PUNC ?))")
    elif word == 'Show':
        return str("(TOP (S (VP (VB Show))) (PUNC .))")