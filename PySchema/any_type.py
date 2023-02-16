from PySchema.exceptions import PySchemException
from typing import Any,Union,List,Dict



def treat_and_get_any(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_type: type=None,
    in_types: list=None,
    expected_value: Any=None,
    inside: list=None,
    not_inside: list=None,
    required:bool=True,
    convert:bool=True,
    default:Any=None
)-> Any:
    """This function is used to treat and get a value from a dict or list."""
    try:
        element = data[key_or_index]
    except Exception:
        if required:
            raise  PySchemException({
                'type': 'KeyError',
                'key_or_index': key_or_index,
                'data': data,
                'menssage': f"#key#:'{key_or_index}' not found in #data# '{data}'",
            })
        else:
            #if is a list and the index is the last position
            if isinstance(key_or_index,int):
                if key_or_index == len(data):
                    data.append(default)
            else:
                data[key_or_index] = default
            
            return default

    
    if convert and expected_type:
        try:
            element = expected_type(element)
            data[key_or_index] = element
        except ValueError:  
            raise PySchemException({
                'type': 'ValueError',
                'key_or_index': key_or_index,
                'data': data,
                'expected_type': expected_type,
                'menssage': f"Value: '{element}' of #key#: '{key_or_index}' can not be converted to '{expected_type.__name__}' on #data# '{data}'",
            })

 


    if expected_value and element != expected_value:
        raise PySchemException({
            'type': 'ValueError',
            'key_or_index': key_or_index,
            'data': data,
            'expected_value': expected_value,
            'menssage': f"Value: '{element}' of #key#: '{key_or_index}' is not '{expected_value}' on #data# '{data}'",
        })
    
    if inside and element not in inside:
        raise PySchemException({
            'type': 'ValueError',
            'key_or_index': key_or_index,
            'data': data,
            'inside': inside,
            'menssage': f"Value: '{element}' of #key#: '{key_or_index}' is  not in '{inside}' on #data# '{data}'",
        })
    
    if not_inside and element in not_inside:
        raise PySchemException({
            'type': 'ValueError',
            'key_or_index': key_or_index,
            'data': data,
            'not_inside': not_inside,
            'menssage': f"Value: '{element}' of #key#: '{key_or_index}'  in '{not_inside}' on #data# '{data}'",
        })
    if expected_type:
        if not isinstance(element, expected_type):
            raise PySchemException({
                'type': 'TypeError',
                'key_or_index': key_or_index,
                'data': data,
                'expected_type': expected_type,
                'menssage': f"Value: '{element}' of #key#: '{key_or_index}'  is not a '{expected_type.__name__}' on #data# '{data}'",
            })
            
    if in_types:
        if not any([isinstance(element, type_) for type_ in in_types]):
            raise PySchemException({
                'type': 'TypeError',
                'key_or_index': key_or_index,
                'data': data,
                'in_types': in_types,
                'menssage': f"Value: '{element}' of #key#: '{key_or_index}'  is not a '{in_types}' on #data# '{data}'",
            })
    return element
    