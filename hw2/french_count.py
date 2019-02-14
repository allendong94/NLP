import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')
    f.initial_state = 'start'
    f.add_state('00x')
    f.add_state('0xx')
    f.add_state('xxx')

    f.add_state('n0x')
    f.add_state('nxx')
    f.add_state('01x')
    f.add_state('0x')
    f.add_state('xx')
    f.add_state('07x')
    f.add_state('08x')
    f.add_state('09x')
    f.add_state('final')
    f.set_final('final')
    # 0
    f.add_arc('start', '0xx', [str(0)], ())
    f.add_arc('0xx', '0x', [str(0)], ())
    f.add_arc('0x', 'final', [str(0)], [kFRENCH_TRANS[0]])
    #1~9
    for ii in xrange(1,10):
        f.add_arc('0x', 'final', [str(ii)], [kFRENCH_TRANS[ii]])
    #10~19[10,11~16,17~19]
    f.add_arc('0xx','01x',[str(1)],())
    for ii in xrange(7):
        f.add_arc('01x','final',[str(ii)],[kFRENCH_TRANS[ii+10]])
    for ii in xrange(7, 10):
        f.add_arc('01x', 'final', [str(ii)], [kFRENCH_TRANS[10],kFRENCH_TRANS[ii]])
    #20~69
    for ii in xrange(2,7):
        f.add_arc('0xx','00x',[str(ii)],[kFRENCH_TRANS[ii*10]])
    f.add_arc('00x','final',[str(0)],())
    f.add_arc('00x','final',[str(1)], [kFRENCH_AND,kFRENCH_TRANS[1]])
    for ii in xrange(2,10):
        f.add_arc('00x','final',[str(ii)],[kFRENCH_TRANS[ii]])
    #7x
    f.add_arc('0xx','07x',[str(7)],[kFRENCH_TRANS[60]])
    f.add_arc('07x', 'final', [str(0)], [kFRENCH_TRANS[10]])
    f.add_arc('07x', 'final', [str(1)], [kFRENCH_AND,kFRENCH_TRANS[11]])
    for ii in xrange(2,7):
        f.add_arc('07x', 'final', [str(ii)], [kFRENCH_TRANS[ii+10]])
    for ii in xrange(7, 10):
        f.add_arc('07x', 'final', [str(ii)], [kFRENCH_TRANS[10],kFRENCH_TRANS[ii]])
    #8x
    f.add_arc('0xx', '08x',[str(8)],[kFRENCH_TRANS[4],kFRENCH_TRANS[20]])
    f.add_arc('08x', 'final', [str(0)], ())
    for ii in xrange(1,10):
        f.add_arc('08x', 'final', [str(ii)], [kFRENCH_TRANS[ii]])
    #9x
    f.add_arc('0xx', '09x',[str(9)],[kFRENCH_TRANS[4],kFRENCH_TRANS[20]])
    for ii in xrange(7):
        f.add_arc('09x','final',[str(ii)],[kFRENCH_TRANS[ii+10]])
    for ii in xrange(7,10):
        f.add_arc('09x','final',[str(ii)],[kFRENCH_TRANS[10],kFRENCH_TRANS[ii]])
    #xxx
    f.add_arc('start','nxx',[str(1)],[kFRENCH_TRANS[100]])
    for ii in xrange(2, 10):
        f.add_arc('start','nxx',[str(ii)],[kFRENCH_TRANS[ii],kFRENCH_TRANS[100]])
    for ii in xrange(2):
        if(ii==0):
           f.add_arc('nxx', 'n0x', [str(0)], ())
           f.add_arc('n0x', 'final', [str(0)], ())
        else:
           f.add_arc('nxx', '01x', [str(1)], ())
    for ii in xrange(2,7):
        f.add_arc('nxx','00x',[str(ii)],[kFRENCH_TRANS[ii*10]])

    for ii in xrange(1,10):
        f.add_arc('n0x', 'final', [str(ii)], [kFRENCH_TRANS[ii]])
    for ii in xrange(7,10):
        if(ii==7):
           f.add_arc('nxx', '07x', [str(7)], [kFRENCH_TRANS[60]])
        elif(ii==8):
           f.add_arc('nxx', '08x', [str(8)], [kFRENCH_TRANS[4],kFRENCH_TRANS[20]])
        elif(ii==9):
           f.add_arc('nxx', '09x', [str(9)], [kFRENCH_TRANS[4],kFRENCH_TRANS[20]])
    return f


if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))

