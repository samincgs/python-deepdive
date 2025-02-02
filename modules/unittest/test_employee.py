import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    
    # use this premade function to instantiate variables that are needed for each test case
    # it is created anew for each case
    def setUp(self):
        self.emp_1 = Employee('Sam', 'Smith', 50000) # instead of repeating it for each test
        self.emp_2 = Employee('John', 'Doe', 30000)
    
    # called after the execution of each test case
    def tearDown(self):
        pass
    
    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Sam.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'John.Doe@email.com')
        
        self.emp_1.first = 'Joe'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.email, 'Joe.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Doe@email.com')
    
    def test_full_name(self):
        self.assertEqual(self.emp_1.full_name, 'Sam Smith')
        self.assertEqual(self.emp_2.full_name, 'John Doe')

        self.emp_1.first = 'Joe'
        self.emp_2.first = 'Jane'
        
        self.assertEqual(self.emp_1.full_name, 'Joe Smith')
        self.assertEqual(self.emp_2.full_name, 'Jane Doe')
        
    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 31500)
        
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Smith/May')
            self.assertEqual(schedule, 'Success')
        
        
        
        
if __name__ == '__main__':
    unittest.main()