import unittest
import myTokenizer

class TestMyTokenizer(unittest.TestCase):
    
    def setUp(self):
        self.t = MyTokenizer()

    def test_tokenize(self):
        s = 'Я не играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_tokenize(self):
        s = 'Я! не, 0играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_tokenize(self):
        s = 'Я98 не 14 играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_tokenize(self):
        s = 'Я !9 не) 43играю'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])

    def test_tokenize(self):
        s = 'Я не играю90'
        self.assertEqual(self.t.tokenize(s), ['Я', 'не', 'играю'])
       
    def test_tokenize(self):
        s = ''
        self.assertEqual(self.t.tokenize(s), [])
      
class TestStringMethods(unittest.TestCase):
    
    def test_tokenize(self):
        s = 'Я не играю'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])
     
    def test_tokenize(self):
        s = 'Я! не, 0играю'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])

    def test_tokenize(self):
        s = 'Я98 не 14 играю'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])

    def test_tokenize(self):
        s = 'Я !9 не) 43играю'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])

    def test_tokenize(self):
        s = 'Я не играю90'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])
        
    def test_tokenize(self):
        s = ''
        self.assertEqual(alpha.letters(s), [])


if __name__ == '__main__':
        unittest.main()
                         

