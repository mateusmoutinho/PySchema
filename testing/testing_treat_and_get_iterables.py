import unittest
import PySchema

class TestTreatAndGetIterables(unittest.TestCase):

    def test_positive_result_with_list(self):
        user_data = {
            'names': ['John'],
        }
        names = PySchema.treat_and_get_iterable(user_data, 'names')
        self.assertEqual(names, ['John'])
    
    def test_positive_result_with_tuple(self):
        user_data = {
            'names': ('John',),
        }
        names = PySchema.treat_and_get_iterable(user_data, 'names')
        self.assertEqual(names, ('John',))
    
    def test_positive_result_with_set(self):
        user_data = {
            'names': {'John'},
        }
        names = PySchema.treat_and_get_iterable(user_data, 'names')
        self.assertEqual(names, {'John'})
    
    def test_positive_result_with_expected_type(self):
        user_data = {
            'names': ['John'],
        }
        names = PySchema.treat_and_get_iterable(user_data, 'names', expected_type=str)
        self.assertEqual(names, ['John'])