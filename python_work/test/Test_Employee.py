import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """ Unit test to test employee.py """

    def setUp(self):
        self.employee = Employee('Wei Han', 'Ngan', 1000000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 1005000)

    def test_give_custom_raise(self):
        self.employee.give_raise(1000000)
        self.assertEqual(self.employee.annual_salary, 2000000)

unittest.main()
