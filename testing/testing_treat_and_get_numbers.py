import unittest
import PySchema

class TestTreatAndGetNumbers(unittest.TestCase):

    def test_positive_result_with_integers(self):
        user_data = {
            'age': 3,
        }
        age = PySchema.treat_and_get_number(user_data, 'age',expected_type=int)
        self.assertEqual(age, 3)
    
    def test_positive_result_with_floats(self):
        user_data = {
            'age': 3.0,
        }
        age = PySchema.treat_and_get_number(user_data, 'age',expected_type=float)
        self.assertEqual(age, 3.0)
 
    def test_positive_result_with_strings(self):
        user_data = {
            'age': '3',
        }
        age = PySchema.treat_and_get_number(user_data, 'age',expected_type=int)
        self.assertEqual(age, 3)
    
    def test_positive_result_with_max(self):
        user_data = {
            'age': 3,
        }
        age = PySchema.treat_and_get_number(user_data, 'age',expected_type=int, max=4)
        self.assertEqual(age, 3)
    
    def test_positive_result_with_min(self):
        user_data = {
            'age': 3,
        }
        age = PySchema.treat_and_get_number(user_data, 'age',expected_type=int, min=2)
        self.assertEqual(age, 3)

    def test_positive_result_with_max_and_min(self):
        user_data = {
            'age': 3,
        }
        age = PySchema.treat_and_get_number(user_data, 'age',expected_type=int, min=2, max=4)
        self.assertEqual(age, 3)
    
    def test_positive_result_with_expected_value(self):
        user_data = {
            'age': 3,
        }
        age = PySchema.treat_and_get_number(user_data, 'age',expected_type=int, expected_value=3)
        self.assertEqual(age, 3)

    def test_positive_result_with_inside(self):
        user_data = {
            'age': 3,
        }
        age = PySchema.treat_and_get_number(user_data, 'age',expected_type=int, inside=[3])
        self.assertEqual(age, 3)
    
    def test_negative_result_not_numbers(self):
        user_data = {
            'age': 'John',
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_number(user_data, 'age',expected_type=int)

    def test_negative_result_with_max(self):
        user_data = {
            'age': 3,
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_number(user_data, 'age',expected_type=int, max=2)
    
    def test_negative_result_with_min(self):
        user_data = {
            'age': 3,
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_number(user_data, 'age',expected_type=int, min=4)

    def test_negative_result_with_max_and_min(self):
        user_data = {
            'age': 3,
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_number(user_data, 'age',expected_type=int, min=4, max=5)

    def test_negative_result_with_expected_value(self):
        user_data = {
            'age': 3,
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_number(user_data, 'age',expected_type=int, expected_value=4)
    
    def test_negative_result_with_inside(self):
        
        user_data = {
            'age': 3,
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_number(user_data, 'age',expected_type=int, inside=[4])
    
    
    def test_negative_result_with_expected_type(self):
        user_data = {
            'age': 3,
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_number(user_data, 'age', convert=False,expected_type=float)
    