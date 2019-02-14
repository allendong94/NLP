import unittest
from soundex import letters_to_numbers, truncate_to_three_digits, add_zero_padding
from french_count import french_count, prepare_input
from morphology import generate

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.f1 = letters_to_numbers()
        self.f2 = truncate_to_three_digits()
        self.f3 = add_zero_padding()

        self.french = french_count()

    def test_letters(self):
        self.assertEqual("".join(self.f1.transduce(x for x in "washington")), "w25235")
        self.assertEqual("".join(self.f1.transduce(x for x in "jefferson")), "j1625")
        self.assertEqual("".join(self.f1.transduce(x for x in "adams")), "a352")
        self.assertEqual("".join(self.f1.transduce(x for x in "bush")), "b2")

    def test_truncation(self):
        self.assertEqual("".join(self.f2.transduce(x for x in "a33333")), "a333")
        self.assertEqual("".join(self.f2.transduce(x for x in "123456")), "123")
        self.assertEqual("".join(self.f2.transduce(x for x in "11")), "11")
        self.assertEqual("".join(self.f2.transduce(x for x in "5")), "5")

    def test_padding(self):
        self.assertEqual("".join(self.f3.transduce(x for x in "3")), "300")
        self.assertEqual("".join(self.f3.transduce(x for x in "b56")), "b560")
        self.assertEqual("".join(self.f3.transduce(x for x in "c111")), "c111")

    def test_numbers(self):
        self.assertEqual(" ".join(self.french.transduce(prepare_input(0))),
                         "zero")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(100))),
                         "cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(31))),
                         "trente et un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(99))),
                         "quatre vingt dix neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(300))),
                         "trois cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(555))),
                         "cinq cent cinquante cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(101))),
                         "cent un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(19))),
                         "dix neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(1))),
                         "un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(2))),
                         "deux")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(3))),
                         "trois")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(4))),
                         "quatre")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(5))),
                         "cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(6))),
                         "six")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(7))),
                         "sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(8))),
                         "huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(9))),
                         "neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(10))),
                         "dix")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(11))),
                         "onze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(12))),
                         "douze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(13))),
                         "treize")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(14))),
                         "quatorze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(15))),
                         "quinze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(16))),
                         "seize")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(17))),
                         "dix sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(18))),
                         "dix huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(19))),
                         "dix neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(20))),
                         "vingt")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(21))),
                         "vingt et un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(22))),
                         "vingt deux")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(23))),
                         "vingt trois")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(24))),
                         "vingt quatre")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(25))),
                         "vingt cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(26))),
                         "vingt six")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(27))),
                         "vingt sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(28))),
                         "vingt huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(29))),
                         "vingt neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(30))),
                         "trente")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(31))),
                         "trente et un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(32))),
                         "trente deux")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(33))),
                         "trente trois")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(34))),
                         "trente quatre")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(35))),
                         "trente cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(36))),
                         "trente six")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(37))),
                         "trente sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(38))),
                         "trente huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(39))),
                         "trente neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(40))),
                         "quarante")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(41))),
                         "quarante et un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(42))),
                         "quarante deux")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(43))),
                         "quarante trois")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(44))),
                         "quarante quatre")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(45))),
                         "quarante cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(46))),
                         "quarante six")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(47))),
                         "quarante sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(48))),
                         "quarante huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(49))),
                         "quarante neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(50))),
                         "cinquante")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(51))),
                         "cinquante et un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(52))),
                         "cinquante deux")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(53))),
                         "cinquante trois")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(54))),
                         "cinquante quatre")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(55))),
                         "cinquante cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(56))),
                         "cinquante six")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(57))),
                         "cinquante sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(58))),
                         "cinquante huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(59))),
                         "cinquante neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(60))),
                         "soixante")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(61))),
                         "soixante et un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(62))),
                         "soixante deux")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(63))),
                         "soixante trois")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(64))),
                         "soixante quatre")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(65))),
                         "soixante cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(66))),
                         "soixante six")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(67))),
                         "soixante sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(68))),
                         "soixante huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(69))),
                         "soixante neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(70))),
                         "soixante dix")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(71))),
                         "soixante et onze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(72))),
                         "soixante douze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(73))),
                         "soixante treize")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(74))),
                         "soixante quatorze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(75))),
                         "soixante quinze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(76))),
                         "soixante seize")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(77))),
                         "soixante dix sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(78))),
                         "soixante dix huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(79))),
                         "soixante dix neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(80))),
                         "quatre vingt")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(81))),
                         "quatre vingt un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(82))),
                         "quatre vingt deux")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(83))),
                         "quatre vingt trois")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(84))),
                         "quatre vingt quatre")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(85))),
                         "quatre vingt cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(86))),
                         "quatre vingt six")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(87))),
                         "quatre vingt sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(88))),
                         "quatre vingt huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(89))),
                         "quatre vingt neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(90))),
                         "quatre vingt dix")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(91))),
                         "quatre vingt onze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(92))),
                         "quatre vingt douze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(93))),
                         "quatre vingt treize")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(94))),
                         "quatre vingt quatorze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(95))),
                         "quatre vingt quinze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(96))),
                         "quatre vingt seize")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(97))),
                         "quatre vingt dix sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(98))),
                         "quatre vingt dix huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(99))),
                         "quatre vingt dix neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(100))),
                         "cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(101))),
                         "cent un")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(102))),
                         "cent deux")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(103))),
                         "cent trois")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(104))),
                         "cent quatre")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(105))),
                         "cent cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(106))),
                         "cent six")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(107))),
                         "cent sept")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(108))),
                         "cent huit")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(109))),
                         "cent neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(110))),
                         "cent dix")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(125))),
                         "cent vingt cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(150))),
                         "cent cinquante")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(175))),
                         "cent soixante quinze")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(200))),
                         "deux cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(250))),
                         "deux cent cinquante")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(300))),
                         "trois cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(350))),
                         "trois cent cinquante")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(400))),
                         "quatre cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(450))),
                         "quatre cent cinquante")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(499))),
                         "quatre cent quatre vingt dix neuf")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(500))),
                         "cinq cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(555))),
                         "cinq cent cinquante cinq")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(600))),
                         "six cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(700))),
                         "sept cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(800))),
                         "huit cent")
        self.assertEqual(" ".join(self.french.transduce(prepare_input(900))),
                         "neuf cent")
    def test_morphology(self):
        self.assertEqual(generate("pack+s"), "packs")
        self.assertEqual(generate("ice+ing"), "icing")
        self.assertEqual(generate("frolic+ed"), "frolicked")
        self.assertEqual(generate("pace+ed"), "paced")
        self.assertEqual(generate("ace+ed"), "aced")
        self.assertEqual(generate("traffic+ing"), "trafficking")
        self.assertEqual(generate("lilac+ing"), "lilacking")
        self.assertEqual(generate("lick+ed"), "licked")

if __name__ == '__main__':
    unittest.main()
