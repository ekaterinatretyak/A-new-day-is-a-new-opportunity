import unittest
import alpha

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_remove(self):
        s = 'Я не играю'
        return s.replace(" ", "")
        self.assertEqual(s.strip(), 'Янеиграю')
        
    def test_split(self):
        s = 'Я не играю'
        self.assertEqual(s.split(), ['Я', 'не', 'играю'])
     
    def test_isnumeric(self):
        self.assertTrue('884569'.isnumeric())
        self.assertFalse('884/играть569'.isnumeric())

    def test_isalpha(self):
        self.assertTrue('Янеиграю'.isalpha())
        self.assertFalse('Я не99 играю!)'.isalpha())

    def test_isalnum(self):
        self.assertTrue('Янеиграю86'.isalnum())
        self.assertFalse('Яне!% играю86?$'.isalnum())
        
if __name__ == '__main__':
    unittest.main()

    
