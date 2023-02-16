import unittest
import PySchema

class TestTreatAndGetAny(unittest.TestCase):

    def test_positive_result_with_dict(self):
        user_data = {
            'name': 'John',
        }
        name = PySchema.treat_and_get_any(user_data, 'name')
        self.assertEqual(name, 'John')

    def test_positive_result_with_list(self):
        user_data = ['John']
        name = PySchema.treat_and_get_any(user_data, 0)
        self.assertEqual(name, 'John')
    
    def test_positive_result_with_expected_type(self):
        user_data = {
            'name': 3,
        }
        name = PySchema.treat_and_get_any(user_data, 'name', expected_type=str)
        self.assertEqual(name, '3')
    

    def test_positive_result_with_expected_value(self):
        user_data = {
            'name': 'John',
        }
        name = PySchema.treat_and_get_any(user_data, 'name', expected_value='John')
        self.assertEqual(name, 'John')
    
    def test_positive_result_with_inside(self):
        user_data = {
            'name': 'John',
        }
        name = PySchema.treat_and_get_any(user_data, 'name', inside=['John'])
        self.assertEqual(name, 'John')
    
    def test_positive_result_with_not_inside(self):
        user_data = {
            'name': 'John',
        }
        name = PySchema.treat_and_get_any(user_data, 'name', not_inside=['Mary'])
        self.assertEqual(name, 'John')
    
    def test_positive_result_with_in_types(self):
        user_data = {
            'name': 'John',
        }
        name = PySchema.treat_and_get_any(user_data, 'name',convert=False, in_types=[str])
        self.assertEqual(name, 'John')
    

    def test_positive_result_with_convert(self):
        user_data = {
            'name': '3',
        }
        name = PySchema.treat_and_get_any(user_data, 'name',expected_type=int, convert=True)
        self.assertEqual(name, 3)
    

    def test_positive_result_with_default(self):
        user_data = {
            'name': 3,
        }
        name = PySchema.treat_and_get_any(user_data, 'name', default='John')
        self.assertEqual(name, 3)

    def test_positive_result_with_default_and_expected_type(self):
        user_data = {
            'name': 3,
        }
        name = PySchema.treat_and_get_any(user_data, 'name', default='John', expected_type=str)
        self.assertEqual(name, '3')
    
    def test_positive_result_with_default_and_expected_value(self):
        user_data = {
            'name': 'John',
        }
        name = PySchema.treat_and_get_any(user_data, 'name', expected_value='John')
        self.assertEqual(name, 'John')
    
    def test_positive_result_with_default_and_inside(self):
        user_data = {
            'name': 'John',
        }
        name = PySchema.treat_and_get_any(user_data, 'name', default='John', inside=['John', 'Mary'])
        self.assertEqual(name, 'John')
    
    def test_positive_result_with_default_and_not_inside(self):
        user_data = {
           
        }
        name = PySchema.treat_and_get_any(user_data, 'name', default='John', not_inside=['Mary'])
        self.assertEqual(name, 'John')
    
    def test_negative_result_with_expected_type(self):
        user_data = {
            'name': 3,
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_any(user_data, 'name',convert=False, expected_type=str)


    def test_negative_result_with_expected_value(self):
        user_data = {
            'name': 'John',
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_any(user_data, 'name', expected_value='Mary')


    def test_negative_result_with_inside(self):
        user_data = {
            'name': 'John',
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_any(user_data, 'name', inside=['Mary'])
        
    def test_negative_result_with_not_inside(self):
        user_data = {
            'name': 'John',
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_any(user_data, 'name', not_inside=['John'])
        
    def test_negative_result_with_in_types(self):
        user_data = {
            'name': 'John',
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_any(user_data, 'name', in_types=[int])
    
    def test_negative_result_with_convert(self):
        user_data = {
            'name': 'John',
        }
        with self.assertRaises(PySchema.PySchemaException):
            PySchema.treat_and_get_any(user_data, 'name', expected_type=int, convert=True)
        
    
   

    