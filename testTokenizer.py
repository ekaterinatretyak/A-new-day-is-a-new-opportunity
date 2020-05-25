import unittest
import myTokenizer
from generator import MyTokenizer
from generator import Token

class TestGenAlphaAndDigit(unittest.TestCase):
    def setUp(self):
        self.k = MyTokenizer()

    def test_alpha(self):
        s = list(self.k.gen_alpha_digit_tokens('я не играю'))
        self.assertEqual(s[0], Token ("я", "ALPHA", 0, 1))
        self.assertEqual(len(s), 3)

    def test_without_space(self):
        s = list(self.k.gen_alpha_digit_tokens('ябудуиграть'))
        self.assertEqual(s, [Token('ябудуиграть', 'ALPHA', 0, 11)])
        self.assertEqual(len(s), 1)

    def test_digitals_string(self):
        s = list(self.k.gen_alpha_digit_tokens('981456'))
        self.assertEqual(len(s), 1)
        self.assertEqual(s, [Token('981456', 'DIGIT', 0, 6)])

    def test_punctuation(self):
        s = list(self.k.gen_alpha_digit_tokens('Я буду!! играть'))
        self.assertEqual(len(s), 3)
        self.assertEqual(s[0], Token('Я', 'ALPHA', 0, 1))

    def test_empty_string(self):
        s = list(self.k.gen_alpha_digit_tokens(''))
        self.assertEqual(len(s), 0)
        self.assertEqual(s, [])

    def test_last_symbol(self):
        s = list(self.k.gen_alpha_digit_tokens('я не буду с тобой играть 00'))
        self.assertEqual(len(s), 7)
        self.assertEqual(s[6], Token('00','DIGIT', 25, 27))


class TestGenerator(unittest.TestCase):  # Check generator of categories
    def setUp(self):
        self.k = MyTokenizer()

    def test_alpha(self):
        s = list(self.k.gen_tokenize_cat('я не играю'))
        self.assertEqual(s[0], Token ("я", "ALPHA", 0, 1))
        self.assertEqual(len(s), 5)

    def test_without_space(self):
        s = list(self.k.gen_tokenize_cat('ябудуиграть'))
        self.assertEqual(s, [Token('ябудуиграть', 'ALPHA', 0, 11)])
        self.assertEqual(len(s), 1)

    def test_digitals_string(self):
        s = list(self.k.gen_tokenize_cat('981456'))
        self.assertEqual(len(s), 1)
        self.assertEqual(s, [Token('981456', 'DIGIT', 0, 6)])

    def test_punctuation(self):
        s = list(self.k.gen_tokenize_cat('Я буду!! играть'))
        self.assertEqual(len(s), 6)
        self.assertEqual(s[3], Token('!!', 'PUNCT', 6, 8))

    def test_empty_string(self):
        s = list(self.k.gen_tokenize_cat(''))
        self.assertEqual(len(s), 0)
        self.assertEqual(s, [])

    def test_last_symbol(self):
        s = list(self.k.gen_tokenize_cat('я не буду с тобой играть 00'))
        self.assertEqual(len(s), 13)
        self.assertEqual(s[12], Token('00','DIGIT', 25, 27))

class TestCategories(unittest.TestCase):  # Check class MyTokenizer, method tokenize_cat

    def setUp(self):
        self.k = MyTokenizer()

    def test_alpha(self):
        s = self.k.tokenize_cat('я не играю')
        self.assertEqual(s[0], Token ("я", "ALPHA", 0, 1))
        self.assertEqual(len(s), 5)

    def test_without_space(self):
        s = self.k.tokenize_cat('ябудуиграть')
        self.assertEqual(s, [Token('ябудуиграть', 'ALPHA', 0, 11)])
        self.assertEqual(len(s), 1)

    def test_digitals_string(self):
        s = self.k.tokenize_cat('981456')
        self.assertEqual(len(s), 1)
        self.assertEqual(s, [Token('981456', 'DIGIT', 0, 6)])

    def test_punctuation(self):
        s = self.k.tokenize_cat('Я буду!! играть')
        self.assertEqual(len(s), 6)
        self.assertEqual(s[3], Token('!!', 'PUNCT', 6, 8))

    def test_empty_string(self):
        s = self.k.tokenize_cat('')
        self.assertEqual(len(s), 0)
        self.assertEqual(s, [])

    def test_last_symbol(self):
        s = self.k.tokenize_cat('я не буду с тобой играть 00')
        self.assertEqual(len(s), 13)
        self.assertEqual(s[12], Token('00','DIGIT', 25, 27))

class TestMyTokenizer(unittest.TestCase): #Check class MyTokenizer, method tokenize

    def setUp(self):
        self.k = MyTokenizer()

    def test_alpha(self):
        s = 'Я не играю'
        self.assertEqual(self.k.tokenize(s), ['Я', 'не', 'играю'])

    def test_punctuation(self):
        s = 'Я! не, играю'
        self.assertEqual(self.k.tokenize(s), ['Я', 'не', 'играю'])

    def test_digitals_string(self):
        s = 'Я98 не 14 играю'
        self.assertEqual(self.k.tokenize(s), ['Я', 'не', 'играю'])

    def test_symbols(self):
        s = 'Я !9 не 43играю'
        self.assertEqual(self.k.tokenize(s), ['Я', 'не', 'играю'])

    def test_digitals(self):
        s = 'Я не играю90'
        self.assertEqual(self.k.tokenize(s), ['Я', 'не', 'играю'])

    def test_empty_string(self):
        s = ''
        self.assertEqual(self.k.tokenize(s), [])


class TestMyFunction(unittest.TestCase): #Check function strspl

    def test_alpha(self):
        s = 'Я не играю'
        self.assertEqual(myTokenizer.strspl(s), ['Я', 'не', 'играю'])

    def test_punctuation(self):
        s = 'Я! не, 0играю'
        self.assertEqual(myTokenizer.strspl(s), ['Я', 'не', 'играю'])

    def test_digitals_string(self):
        s = 'Я98 не 14 играю'
        self.assertEqual(myTokenizer.strspl(s), ['Я', 'не', 'играю'])

    def test_symbols(self):
        s = 'Я !9 не) 43играю'
        self.assertEqual(myTokenizer.strspl(s), ['Я', 'не', 'играю'])

    def test_digitals(self):
        s = 'Я не играю90'
        self.assertEqual(myTokenizer.strspl(s), ['Я', 'не', 'играю'])

    def test_empty_string(self):
        s = ''
        self.assertEqual(myTokenizer.strspl(s), [])

if __name__ == '__main__':
    unittest.main()
