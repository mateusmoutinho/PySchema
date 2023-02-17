from PySchema.exceptions import PySchemaException
from typing import Any


def check_type(element:Any,expected_type:type=None,in_types:list=None):
    if expected_type:
        in_types = [expected_type]
    elif in_types:
        pass 
    else:
        raise Exception('expected_type or in_types is required')
    
    for expected_type in in_types:
        if isinstance(element,expected_type):
            return True
    raise PySchemaException({
        'type': 'TypeError',
        'element': element,
        'expected_type': expected_type,
        'menssage': f"element:'{element}' is not  '{in_types[0].__name__}'"
    })

    