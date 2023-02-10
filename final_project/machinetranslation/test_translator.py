import unittest

from translator import english_to_french, french_to_english

class TestEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"),"Bonjour") 
        self.assertNotEqual(english_to_french("Hello"),None)
        

class TestFranch(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"),"Hello") 
        self.assertNotEqual(french_to_english("Bonjour"),None)
unittest.main()