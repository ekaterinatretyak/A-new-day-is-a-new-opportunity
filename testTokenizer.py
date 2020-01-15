import unittest
import myTokenizer

class TestMyTokenizer(unittest.TestCase):
    
    def setUp(self):
        self.t = myTokenizer.MyTokenizer()

    def test_tokenize(self):
        s = 'Я не играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_punctuation(self):
        s = 'Я! не, 0играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_digitals_string(self):
        s = 'Я98 не 14 играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_symbols(self):
        s = 'Я !9 не) 43играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_digitals(self):
        s = 'Я не играю90'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])
       
    def test_empty_string(self):
        s = ''
        self.assertEqual(self.t.tokenize(s), [])
      
class TestStringMethods(unittest.TestCase):
    
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
                         

