import unittest
import myTokenizer

class TestMyTokenizer(unittest.TestCase):

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
        self.assertEqual(myTokenizer.tokenize(s), [])

    def test_tokenize(self):
        s = 'Я не играю!'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])
        

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

    def test_tokenize(self):
        s = 'Я не играю!'
        self.assertEqual(myTokenizer.tokenize(s), ['Я', 'не', 'играю'])


if __name__ == '__main__':
        unittest.main()
                         

