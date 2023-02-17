from PySchema.exceptions import PySchemaException
from typing import Any,Union,List,Dict,Callable



def treat_and_get_any(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_type: type=None,
    in_types: List[Any]=None,
    expected_value: Any=None,
    inside: list=None,
    not_inside: list=None,
    required:bool=True,
    convert:bool=False,
    default:Any=None,
    treater:Callable=None,
)-> Any:
    """This function is used to treat and get a value from a dict or list.
    
    Args:
        data (Union[dict,list]): The dict or list to be treated.
        key_or_index (Union[int,str]): The key or index to be treated.
        expected_type (type, optional): The expected type of the value. Defaults to None.
        in_types (List[Any], optional): The expected types of the value. Defaults to None.
        expected_value (Any, optional): The expected value of the value. Defaults to None.
        inside (list, optional): The expected values of the value. Defaults to None.
        not_inside (list, optional): The not expected values of the value. Defaults to None.
        required (bool, optional): If the value is required. Defaults to True.
        convert (bool, optional): If the value can be converted. Defaults to False.
        default (Any, optional): The default value if the value is not required. Defaults to None.    
        treater (Callable, optional): A function to treat the value. Defaults to None.
    Returns:
        Any: The value treated.
    """
    try:
        element = data[key_or_index]
    except Exception:
        if default is not None:
            #if is a list and the index is the last position
            if isinstance(key_or_index,int):
                if key_or_index == len(data):
                    data.append(default)
            else:
                element = default
                data[key_or_index] = default

        elif required:
            raise  PySchemaException({
                'type': 'NotFountError',
                'key_or_index': key_or_index,
                'data': data,
                'menssage': f"#key#:'{key_or_index}' not found in #data# '{data}'",
            })
       

    #for avoid convert with lists
    if convert and in_types:
        convert = False



    if convert and expected_type:
        try:
            element = expected_type(element)
            data[key_or_index] = element
        except ValueError:  
            raise PySchemaException({
                'type': 'NotConvertError',
                'key_or_index': key_or_index,
                'data': data,
                'expected_type': expected_type,
                'menssage': f"Value: '{element}' of #key#: '{key_or_index}' can not be converted to '{expected_type.__name__}' on #data# '{data}'",
            })

 
    if expected_value and element != expected_value:
        raise PySchemaException({
            'type': 'NotEqualError',
            'key_or_index': key_or_index,
            'data': data,
            'expected_value': expected_value,
            'menssage': f"Value: '{element}' of #key#: '{key_or_index}' is not '{expected_value}' on #data# '{data}'",
        })
    
    if inside and element not in inside:
        raise PySchemaException({
            'type': 'NotInError',
            'key_or_index': key_or_index,
            'data': data,
            'inside': inside,
            'menssage': f"Value: '{element}' of #key#: '{key_or_index}' is  not in '{inside}' on #data# '{data}'",
        })
    
    if not_inside and element in not_inside:
        raise PySchemaException({
            'type': 'InError',
            'key_or_index': key_or_index,
            'data': data,
            'not_inside': not_inside,
            'menssage': f"Value: '{element}' of #key#: '{key_or_index}'  in '{not_inside}' on #data# '{data}'",
        })
    if expected_type:
        if not isinstance(element, expected_type):
            raise PySchemaException({
                'type': 'TypeError',
                'key_or_index': key_or_index,
                'data': data,
                'expected_type': expected_type,
                'menssage': f"Value: '{element}' of #key#: '{key_or_index}'  is not a '{expected_type.__name__}' on #data# '{data}'",
            })
            
    if in_types:
        if not any([isinstance(element, type_) for type_ in in_types]):
            raise PySchemaException({
                'type': 'InTypeError',
                'key_or_index': key_or_index,
                'data': data,
                'in_types': in_types,
                'menssage': f"Value: '{element}' of #key#: '{key_or_index}'  is not a '{in_types}' on #data# '{data}'",
            })
    

    if treater:
        element = treater(element)
        data[key_or_index] = element
    
    return element
    