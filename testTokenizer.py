import unittest
import myTokenizer
from myTokenizer import myTokenizer
from myTokenizer import Token

class TestMyTokenizerCategories(unittest.TestCase):  # Check class MyTokenizer, method tokenize_categories
    
    def setUp(self):
      self.t = myTokenizer.MyTokenizer()
    
    def test_tokenize(self):
        s = self.t.tokenize_categories('Я не играю')
        self.assertEqual(s[0], Token("я", "alpha", 0, 1))
        self.assertEqual(len(s), 5)
    
    def test_punctuation(self):
        s = self.t.tokenize_categories('Я! не, играю')
        self.assertEqual(len(s), 7)
        self.assertEqual(s[1], Token('!', 'punct', 1, 2))
        self.assertEqual(s[5], Token(',', 'punct', 5, 6))
                
    def test_digitals_string(self):
        s = self.t.tokenize_categories('Я98 не 14 играю')
        self.assertEqual(len(s), 8)
        self.assertEqual(s[1], Token('98', 'digit', 1, 3))
        self.assertEqual(s[6], Token('14', 'digit', 7, 9))
        
    def test_symbols(self):
        s = self.t.tokenize_categories('Я !9 не) 43играю')
        self.assertEqual(len(s), 10)
        self.assertEqual(s[2], Token('!', 'punct', 2, 3))
        self.assertEqual(s[3], Token('9', 'digit', 3, 4))
        self.assertEqual(s[6], Token(')', 'punct', 7, 8))
        self.assertEqual(s[8], Token('43', 'digit', 9, 11))
        
    def test_digitals(self):
        s = self.t.tokenize_categories('Я не играю90')
        self.assertEqual(len(s), 5)
        self.assertEqual(s[5], Token('90', 'digit', 10, 12))
       
    def test_empty_string(self):
        s = self.t.tokenize_categories('')
        self.assertEqual(len(s), 0)
        self.assertEqual(s, [])   


class TestMyTokenizer(unittest.TestCase): #Check class MyTokenizer, method tokenize
    
    def setUp(self):
        self.t = myTokenizer.MyTokenizer()

    def test_tokenize(self):
        s = 'Я не играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_punctuation(self):
        s = 'Я! не, играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_digitals_string(self):
        s = 'Я98 не 14 играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_symbols(self):
        s = 'Я !9 не 43играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_digitals(self):
        s = 'Я не играю90'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])
       
    def test_empty_string(self):
        s = ''
        self.assertEqual(self.t.tokenize(s), [])
      
class TestStringMethods(unittest.TestCase): #Check function tokenize
    
    def test_tokenize(self):
        s = 'Я не играю'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])
     
    def test_punctuation(self):
        s = 'Я! не, 0играю'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])

    def test_digitals_string(self):
        s = 'Я98 не 14 играю'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])

    def test_symbols(self):
        s = 'Я !9 не) 43играю'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])

    def test_digitals(self):
        s = 'Я не играю90'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])
        
    def test_empty_string(self):
        s = ''
        self.assertEqual(myTokenizer.tokenize(s), [])


if __name__ == '__main__':
        unittest.main()
                         

