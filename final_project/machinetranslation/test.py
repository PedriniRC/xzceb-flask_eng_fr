'''
Test for the modules in translator
'''
import unittest

from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase):
    def test1(self):
        actual = english_to_french('Hello')
        expected = 'Bonjour'
        self.assertEqual(actual, expected) # test when the string 'Hello' is given as input, the output should be 'Bonjour'.

    def test2(self):
        actual_1 = english_to_french('Cat')
        expected_2 = 'chat'
        self.assertNotEqual(actual_1, expected_2) # test when the string 'Cat' is given as input, the output should not be 'chat'.   

class Test_french_to_english(unittest.TestCase):
    def test3(self):
        actual_3 = french_to_english('Bonjour')
        expected_3 = 'Hello'
        self.assertEqual(actual_3, expected_3) # test when the string 'Bonjour' is given as input, the output should be 'Hello'.

    def test4(self):
        actual_4 = french_to_english('Chien')
        expected_4 = 'dog'
        self.assertNotEqual(actual_4, expected_4) #test when the string 'Chien" is given as input, the output should not be 'dog'.       

if __name__=='__main__':
    unittest.main()        


    