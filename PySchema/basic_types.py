from typing import Any,Union,List,Dict,Callable
from PySchema.complex_types import treat_and_get_iterable,treat_and_get_number
from PySchema.any_types import treat_and_get_any



def treat_and_get_dict(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_value:dict=None,
    inside:List[dict]=None,
    not_inside:List[dict]=None,
    required:dict=True,
    default:dict=None,
    treater:Callable=None,
    max_len:int=None,
    min_len:int=None
)-> dict:
    """This function is used to treat and get a dict from a dict or list.
    Args:
        data (Union[dict,list]): The dict or list to be treated.
        key_or_index (Union[int,str]): The key or index to be treated.
        expected_value (dict, optional): The expected value of the dict. Defaults to None.
        inside (List[dict], optional): The expected values of the dict. Defaults to None.
        not_inside (List[dict], optional): The not expected values of the dict. Defaults to None.
        required (dict, optional): If the dict is required. Defaults to True.
        default (dict, optional): The default value if the dict is not required. Defaults to None.
        treater (Callable, optional): The function to treat the value. Defaults to None.
        max_len (int, optional): The max length of the dict. Defaults to None.
        min_len (int, optional): The min length of the dict. Defaults to None.
    Returns:
        dict: The treated dict.
    """
    return treat_and_get_iterable(
        data=data,
        key_or_index=key_or_index,
        expected_type=dict,
        expected_value=expected_value,
        inside=inside,
        not_inside=not_inside,
        required=required,
        convert=False,
        default=default,
        treater=treater,
        max_len=max_len,
        min_len=min_len
    )

def treat_and_get_str(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_value:str=None,
    inside:List[str]=None,
    not_inside:List[str]=None,
    required:bool=True,
    convert:bool=False,
    default:str=None,
    treater:Callable=None,
    max_len:int=None,
    min_len:int=None
)-> str:
    """
    This function is used to treat and get a str from a dict or list.

    Args:
        data (Union[dict,list]): The dict or list to be treated.
        key_or_index (Union[int,str]): The key or index to be treated.
        expected_value (str, optional): The expected value of the str. Defaults to None.
        inside (List[str], optional): The expected values of the str. Defaults to None.
        not_inside (List[str], optional): The not expected values of the str. Defaults to None.
        required (bool, optional): If the str is required. Defaults to True.
        convert (bool, optional): If the str must be converted. Defaults to False.
        default (str, optional): The default value if the str is not required. Defaults to None.
        treater (Callable, optional): The function to treat the value. Defaults to None.
        max_len (int, optional): The max length of the str. Defaults to None.
        min_len (int, optional): The min length of the str. Defaults to None.
    
    Returns:
        str: The treated str.

    """
    return treat_and_get_iterable(
        data=data,
        key_or_index=key_or_index,
        expected_type=str,
        expected_value=expected_value,
        inside=inside,
        not_inside=not_inside,
        required=required,
        convert=convert,
        default=default,
        treater=treater,
        max_len=max_len,
        min_len=min_len
        
    )

def treat_and_get_list(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_value:list=None,
    inside:List[list]=None,
    not_inside:List[list]=None,
    required:bool=True,
    default:list=None,
    treater:Callable=None,
    max_len:int=None,
    min_len:int=None
)-> list:
    """This function is used to treat and get a list from a dict or list.
    Args:
        data (Union[dict,list]): The dict or list to be treated.
        key_or_index (Union[int,str]): The key or index to be treated.
        expected_value (list, optional): The expected value of the list. Defaults to None.
        inside (List[list], optional): The expected values of the list. Defaults to None.
        not_inside (List[list], optional): The not expected values of the list. Defaults to None.
        required (bool, optional): If the list is required. Defaults to True.
        default (list, optional): The default value if the list is not required. Defaults to None.
        treater (Callable, optional): The function to treat the value. Defaults to None.
        max_len (int, optional): The max length of the list. Defaults to None.
        min_len (int, optional): The min length of the list. Defaults to None.
    Returns:
        list: The treated list.
    """
    return treat_and_get_iterable(
        data=data,
        key_or_index=key_or_index,
        expected_type=list,
        expected_value=expected_value,
        inside=inside,
        not_inside=not_inside,
        required=required,
        convert=False,
        default=default,
        treater=treater,
        max_len=max_len,
        min_len=min_len
    )


def treat_and_get_int(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_value:int=None,
    inside:List[int]=None,
    not_inside:List[int]=None,
    required:bool=True,
    convert:bool=True,
    default:int=None,
    treater:Callable=None,
    max:int=None,
    min:int=None
)-> int:
    """This function is used to treat and get a int from a dict or list.

    Args:
    
        data (Union[dict,list]): The dict or list to be treated.
        key_or_index (Union[int,str]): The key or index to be treated.
        expected_value (int, optional): The expected value of the int. Defaults to None.
        inside (List[int], optional): The expected values of the int. Defaults to None.
        not_inside (List[int], optional): The not expected values of the int. Defaults to None.
        required (bool, optional): If the int is required. Defaults to True.
        convert (bool, optional): If the int must be converted. Defaults to True.
        default (int, optional): The default value if the int is not required. Defaults to None.
        treater (Callable, optional): The function to treat the value. Defaults to None.
        max (int, optional): The max value of the int. Defaults to None.
        min (int, optional): The min value of the int. Defaults to None. 
    
    Returns:
        int: The treated int.
     """
    return treat_and_get_number(
        data=data,
        key_or_index=key_or_index,
        expected_type=int,
        expected_value=expected_value,
        inside=inside,
        not_inside=not_inside,
        required=required,
        convert=convert,
        default=default,
        treater=treater,
        max=max,
        min=min
    )


def treat_and_get_bool(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_value:bool=None,
    required:bool=True,
    convert:bool=True,
    default:int=None,
    treater:Callable=None
)-> bool:
    """This function is used to treat and get a int from a dict or list.

    Args:
    
        data (Union[dict,list]): The dict or list to be treated.
        key_or_index (Union[int,str]): The key or index to be treated.
        expected_value (bool, optional): The expected value of the bool. Defaults to None.
        required (bool, optional): If the bool is required. Defaults to True.
        convert (bool, optional): If the bool must be converted. Defaults to True.
        default (bool, optional): The default value if the bool is not required. Defaults to None.
        treater (Callable, optional): The function to treat the value. Defaults to None.
    Returns:
        bool: The treated bool.
     """
    return treat_and_get_any(
        data=data,
        key_or_index=key_or_index,
        expected_type=bool,
        expected_value=expected_value,
        required=required,
        convert=convert,
        default=default,
        treater=treater
    )


def treat_and_get_float(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_value:float=None,
    inside:List[float]=None,
    not_inside:List[float]=None,
    required:bool=True,
    convert:bool=True,
    default:float=None,
    treater:Callable=None,
    max:float=None,
    min:float=None
)-> float:
    """This function is used to treat and get a float from a dict or list.
    Args:
        data (Union[dict,list]): The dict or list to be treated.
        key_or_index (Union[int,str]): The key or index to be treated.
        expected_value (float, optional): The expected value of the float. Defaults to None.
        inside (List[float], optional): The expected values of the float. Defaults to None.
        not_inside (List[float], optional): The not expected values of the float. Defaults to None.
        required (bool, optional): If the float is required. Defaults to True.
        convert (bool, optional): If the float must be converted. Defaults to True.
        default (float, optional): The default value if the float is not required. Defaults to None.
        treater (Callable, optional): The function to treat the value. Defaults to None.
        max (float, optional): The max value of the float. Defaults to None.
        min (float, optional): The min value of the float. Defaults to None.
    Returns:
        float: The treated float.
        
    """
    return treat_and_get_number(
        data=data,
        key_or_index=key_or_index,
        expected_type=float,
        expected_value=expected_value,
        inside=inside,
        not_inside=not_inside,
        required=required,
        convert=convert,
        default=default,
        treater=treater,
        max=max,
        min=min

    )


