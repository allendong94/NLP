from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """

    remove_list=['a','e','h','i','o','u','w','y']
    change_1 = ['b','f','p','v']
    change_2 = ['c','g','j','k','q','s','x','z']
    change_3 = ['d','t']
    change_4 = ['l']
    change_5 = ['m','n']
    change_6 = ['r']

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('r')
    f1.add_state('s1')
    f1.add_state('s2')
    f1.add_state('s3')
    f1.add_state('s4')
    f1.add_state('s5')
    f1.add_state('s6')
    f1.add_state('1')
    f1.add_state('2')
    #f1.add_state('2')


    f1.initial_state = '1'

    # Set all the final states
    f1.set_final('r')
    f1.set_final('s1')
    f1.set_final('s2')
    f1.set_final('s3')
    f1.set_final('s4')
    f1.set_final('s5')
    f1.set_final('s6')


    # Add the rest of the arcs
    for letter in string.ascii_lowercase:
        f1.add_arc('1', '2', (letter), (letter))
        if(letter.lower() in remove_list):
            f1.add_arc('2','r',(letter),())
            f1.add_arc('r', 'r', (letter), ())
            f1.add_arc('s1', 'r', (letter), ())
            f1.add_arc('s2', 'r', (letter), ())
            f1.add_arc('s3', 'r', (letter), ())
            f1.add_arc('s4', 'r', (letter), ())
            f1.add_arc('s5', 'r', (letter), ())
            f1.add_arc('s6', 'r', (letter), ())
        elif (letter.lower() in change_1):
            f1.add_arc('2', 's1', (letter), ('1'))
            f1.add_arc('r', 's1', (letter), ('1'))
            f1.add_arc('s1', 's1', (letter), ())
            f1.add_arc('s2', 's1', (letter), ('1'))
            f1.add_arc('s3', 's1', (letter), ('1'))
            f1.add_arc('s4', 's1', (letter), ('1'))
            f1.add_arc('s5', 's1', (letter), ('1'))
            f1.add_arc('s6', 's1', (letter), ('1'))
        elif (letter.lower() in change_2):
            f1.add_arc('2', 's2', (letter), ('2'))
            f1.add_arc('r', 's2', (letter), ('2'))
            f1.add_arc('s1', 's2', (letter), ('2'))
            f1.add_arc('s2', 's2', (letter), ())
            f1.add_arc('s3', 's2', (letter), ('2'))
            f1.add_arc('s4', 's2', (letter), ('2'))
            f1.add_arc('s5', 's2', (letter), ('2'))
            f1.add_arc('s6', 's2', (letter), ('2'))
        elif (letter.lower() in change_3):
            f1.add_arc('2', 's3', (letter), ('3'))
            f1.add_arc('r', 's3', (letter), ('3'))
            f1.add_arc('s3', 's3', (letter), ())
            f1.add_arc('s1', 's3', (letter), ('3'))
            f1.add_arc('s2', 's3', (letter), ('3'))
            f1.add_arc('s4', 's3', (letter), ('3'))
            f1.add_arc('s5', 's3', (letter), ('3'))
            f1.add_arc('s6', 's3', (letter), ('3'))
        elif (letter.lower() in change_4):
            f1.add_arc('2', 's4', (letter), ('4'))
            f1.add_arc('r', 's4', (letter), ('4'))
            f1.add_arc('s4', 's4', (letter), ())
            f1.add_arc('s1', 's4', (letter), ('4'))
            f1.add_arc('s2', 's4', (letter), ('4'))
            f1.add_arc('s3', 's4', (letter), ('4'))
            f1.add_arc('s5', 's4', (letter), ('4'))
            f1.add_arc('s6', 's4', (letter), ('4'))
        elif (letter.lower() in change_5):
            f1.add_arc('2', 's5', (letter), ('5'))
            f1.add_arc('r', 's5', (letter), ('5'))
            f1.add_arc('s5', 's5', (letter), ())
            f1.add_arc('s1', 's5', (letter), ('5'))
            f1.add_arc('s2', 's5', (letter), ('5'))
            f1.add_arc('s3', 's5', (letter), ('5'))
            f1.add_arc('s4', 's5', (letter), ('5'))
            f1.add_arc('s6', 's5', (letter), ('5'))
        elif (letter.lower() in change_6):
            f1.add_arc('2', 's6', (letter), ('6'))
            f1.add_arc('r', 's6', (letter), ('6'))
            f1.add_arc('s6', 's6', (letter), ())
            f1.add_arc('s1', 's6', (letter), ('6'))
            f1.add_arc('s2', 's6', (letter), ('6'))
            f1.add_arc('s3', 's6', (letter), ('6'))
            f1.add_arc('s4', 's6', (letter), ('6'))
            f1.add_arc('s5', 's6', (letter), ('6'))
    return f1


    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?


def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final state
    f2.add_state('0')
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')

    f2.initial_state = '0'

    f2.set_final('0')
    f2.set_final('1')
    f2.set_final('2')
    f2.set_final('3')
    # Add the arcs
    for letter in string.letters:
        f2.add_arc('0', '0', (letter), (letter))

    for n in xrange(10):
        f2.add_arc('0', '1', (str(n)), (str(n)))
        f2.add_arc('1', '2', (str(n)), (str(n)))
        f2.add_arc('2', '3', (str(n)), (str(n)))
        f2.add_arc('3', '3', (str(n)), ())

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?


def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')
    f3.add_state('0')
    f3.add_state('1')
    f3.add_state('2a')
    f3.add_state('2')
    f3.add_state('3')

    f3.initial_state = '0'
    f3.set_final('3')
    for letter in string.letters:
        f3.add_arc('0', '0', (letter), (letter))
    for number in xrange(10):
        f3.add_arc('0', '1', (str(number)), (str(number)))
        f3.add_arc('1', '2', (str(number)), (str(number)))
        f3.add_arc('2', '3', (str(number)), (str(number)))
        f3.add_arc('2', '3', (), ('0'))
        f3.add_arc('1', '2a', (), ('0'))
        f3.add_arc('2a', '3', (), ('0'))
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!


if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
