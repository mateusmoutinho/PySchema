from PySchema.exceptions import PySchemaException
from typing import Any


def check_type(data:Any,expected_type:type=None,in_types:list=None):
    """Check if element is instance of expected_type or in_types
    Args:
        element (Any): element to check
        expected_type (type, optional): type to check. Defaults to None.
        in_types (list, optional): list of types to check. Defaults to None
    """
    if expected_type:
        in_types = [expected_type]
    elif in_types:
        pass 
    else:
        raise Exception('expected_type or in_types is required')
    
    for expected_type in in_types:
        if isinstance(data,expected_type):
            return True
    raise PySchemaException({
        'type': 'TypeError',
        'data': data,
        'expected_type': expected_type,
        'menssage': f"element:'{data}' is not  '{in_types[0].__name__}'"
    })


def ensure_not_expected_keys_is_present(data:dict,expected_keys:list):
    """Ensure that data has not keys that are not in expected_keys
    Args:
        data (dict): data to check
        expected_keys (list): list of expected keys
    """
    for key in data.keys():
        if key not in expected_keys:
            raise PySchemaException({
                'type': 'NotExpectedKeyError',
                'data': data,
                'key_or_index': key,
                'expected_keys': expected_keys,
                'menssage': f"key:'{key}' is not in '{expected_keys}'"
            })