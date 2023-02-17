from PySchema.exceptions import PySchemaException
from typing import Any,Union,List,Dict,Callable
from PySchema.any_types import treat_and_get_any


 

def treat_and_get_number(
    data:dict or list,
    key_or_index:int or str,
    expected_type:type,
    expected_value:float or int=None,
    inside:List[Union[list,float]]=None,
    not_inside:List[Union[list,float]]=None,
    required:bool=True,
    convert:bool=True,
    default:Union[int,float]=None,
    treater:Callable=None,
    max:float or int=None,
    min:float or int=None,

)-> int or float:
    """ This function is used to treat and get a number from a dict or list.
    Args:
        data (Union[dict,list]): The dict or list to be treated.
        key_or_index (Union[int,str]): The key or index to be treated.
        expected_type (type): The expected type of the value.
        expected_value (Union[float,int], optional): The expected value of the value. Defaults to None.
        inside (list, optional): The expected values of the value. Defaults to None.
        not_inside (list, optional): The not expected values of the value. Defaults to None.
        required (bool, optional): If the value is required. Defaults to True.
        convert (bool, optional): If the value can be converted. Defaults to True.
        default (Any, optional): The default value if the value is not required. Defaults to None.
        treater (Callable, optional): The function to treat the value. Defaults to None.
        max (Union[float,int], optional): The max value of the value. Defaults to None.
        min (Union[float,int], optional): The min value of the value. Defaults to None.

    Returns:
        Union[int,float]: The value treated.    
    """
    value = treat_and_get_any(
        data=data,
        key_or_index=key_or_index,
        expected_type=expected_type,
        in_types=None,
        expected_value=expected_value,
        inside=inside,
        not_inside=not_inside,
        required=required,
        convert=convert,
        default=default,
        treater=treater,
    )
    if value:
        if max and value > max:
            raise PySchemaException({
                'type': 'MaxValueError',
                'key_or_index': key_or_index,
                'data': data,
                'max': max,
                'menssage': f"Value: '{value}' of #key#: '{key_or_index}' is greater than '{max}' on #data# '{data}'",
            })
        if min and value < min:
            raise  PySchemaException({
                'type': 'MinValueError',
                'key_or_index': key_or_index,
                'data': data,
                'min': min,
                'menssage': f"Value: '{value}' of #key#: '{key_or_index}' is less than '{min}' on #data# '{data}'",

            })
    return value


def treat_and_get_iterable(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_type: type,
    expected_value: Any=None,
    inside: list=None,
    not_inside: list=None,
    required:bool=True,
    convert:bool=False,
    default:Any=None,
    treater:Callable=None,
    max_len:int=None,
    min_len:int=None
)-> Union[list,str,dict,tuple,set]:
    """ This function is used to treat and get a iterable from a dict or list.
    Args:
        data (Union[dict,list]): The dict or list to be treated.
        key_or_index (Union[int,str]): The key or index to be treated.
        expected_type (type): The expected type of the value.
        expected_value (Any, optional): The expected value of the value. Defaults to None.
        inside (list, optional): The expected values of the value. Defaults to None.
        not_inside (list, optional): The not expected values of the value. Defaults to None.
        required (bool, optional): If the value is required. Defaults to True.
        convert (bool, optional): If the value can be converted. Defaults to False.
        default (Any, optional): The default value if the value is not required. Defaults to None.
        treater (Callable, optional): The function to treat the value. Defaults to None.
        max_len (int, optional): The max length of the value. Defaults to None.
        min_len (int, optional): The min length of the value. Defaults to None.
    Returns:
        Union[list,str]: The value treated.
    """
    
    value = treat_and_get_any(
        data=data,
        key_or_index=key_or_index,
        expected_type=expected_type,
        in_types=None,
        expected_value=expected_value,
        inside=inside,
        not_inside=not_inside,
        required=required,
        convert=convert,
        default=default,
        treater=treater,
    )
    if value:
        if max_len and len(value) > max_len:
            raise  PySchemaException({
                'type': 'MaxLenError',
                'key_or_index': key_or_index,
                'data': data,
                'max_len': max_len,
                'menssage': f"Length of {value} is greater than {max_len}",
            })
        if min_len and len(value) < min_len:
            raise PySchemaException({
                'type': 'MinLenError',
                'key_or_index': key_or_index,
                'data': data,
                'min_len': min_len,
                'menssage': f"Length of {value} is less than {min_len}",
            })

    return value

