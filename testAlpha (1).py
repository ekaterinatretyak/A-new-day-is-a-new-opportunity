import unittest
import alpha

class TestStringMethods(unittest.TestCase):
    
    def test_letters(self):
        s = 'Я не играю'
        self.assertEqual(alpha.letters(s), ['Я', 'не', 'играю'])
     
    def test_letters(self):
        s = 'Я! не, 0играю'
        self.assertEqual(alpha.letters(s), ['Я', 'не', 'играю'])

    def test_letters(self):
        s = 'Я98 не 14 играю'
        self.assertEqual(alpha.letters(s), ['Я', 'не', 'играю'])

    def test_letters(self):
        s = 'Я !9 не) 43играю'
        self.assertEqual(alpha.letters(s), ['Я', 'не', 'играю'])

    def test_letters(self):
        s = 'Я не играю90'
        self.assertEqual(alpha.letters(s), ['Я', 'не', 'играю'])

    def test_letters(self):
        s = ''
        self.assertEqual(alpha.letters(s), [])


if __name__ == '__main__':
        unittest.main()


