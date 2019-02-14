import numpy as np
import sys
def run_viterbi(emission_scores, trans_scores, start_scores, end_scores):
    """Run the Viterbi algorithm.

    N - number of tokens (length of sentence)
    L - number of labels

    As an input, you are given:
    - Emission scores, as an NxL array
    - Transition scores (Yp -> Yc), as an LxL array
    - Start transition scores (S -> Y), as an Lx1 array
    - End transition scores (Y -> E), as an Lx1 array

    You have to return a tuple (s,y), where:
    - s is the score of the best sequence
    - y is a size N array of integers representing the best sequence.
    """
    L = start_scores.shape[0]
    assert end_scores.shape[0] == L
    assert trans_scores.shape[0] == L
    assert trans_scores.shape[1] == L
    assert emission_scores.shape[1] == L
    N = emission_scores.shape[0]

    y = []
    back = np.zeros((L,N),dtype=np.int32)
    vals = np.zeros((L,N))
    for i in xrange(L):
         vals[i][0] = start_scores[i] + emission_scores[0,i]
    for i in xrange(1, N ):
        for j in xrange( L ):
            score_max = -sys.maxint-1
            for k in xrange( L ):
                s = vals[k][i-1]+trans_scores[k][j]+emission_scores[i][j]
                if s > score_max:
                    score_max = s
                    back[j][i] = k
            vals[j][i] = score_max
    for i in xrange( L ):
        vals[i][-1]= vals[i][-1] + end_scores[i]

    s = -sys.maxint -1
    index = -1
    for i in xrange(L):
        if vals[i][-1] >s:
            s = vals[i][-1]
            index = i
    i = N-1
    while(i != -1):
        y = [index] + y
        index = back[index][i]
        i -=1
    # score set to 0
    return (s, y)
