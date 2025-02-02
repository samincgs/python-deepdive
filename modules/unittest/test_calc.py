# The naming convention when writing tests is test_filename
import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        # usually used to test edge cases
        self.assertEqual(calc.add(10, 5), 15)
        # check negative and positive number
        self.assertEqual(calc.add(-1, 1), 0)
        # check two negative numbers
        self.assertEqual(calc.add(-1, -1), -2)
    
    def test_sub(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    
    def test_mult(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        
        self.assertRaises(ValueError, calc.divide, 10, 0) # or with self.assertRaises(ValueError): calc.divide(10, 0)
        
        

        
        
if __name__ == '__main__':
    unittest.main()