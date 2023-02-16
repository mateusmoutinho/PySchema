from typing import Any,Union,List,Dict
from PySchema.complex_types import treat_and_get_iterable,treat_and_get_number




def treat_and_get_dict(
    data: Union[dict,list],
    key_or_index:Union[int,str],
    expected_value:dict=None,
    inside:List[dict]=None,
    not_inside:List[dict]=None,
    required:dict=True,
    default:dict=None,
    max_len:int=None,
    min_len:int=None
)-> dict:
    """This function is used to treat and get a dict from a dict or list.
    Args:
        data (Union[dict,list]): The data to be treated.
        key_or_index:(int or str) key or index to be treated.
        expected_value (dict): The expected value of the key or index.
        inside (List[dict]): The expected values of the key or index.
        not_inside (List[dict]): The expected values of the key or index.
        required (bool): If the key or index is required.
        default (dict): The default value if the key or index is not required.
        max_len (int): The maximum length of the value.
        min_len (int): The minimum length of the value.
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
    max_len:int=None,
    min_len:int=None
)-> str:
    """
    This function is used to treat and get a str from a dict or list.

    Args:

        data:(dict or list) data to be treated.
        key_or_index:(int or str) key or index to be treated.
        expected_value:(str) expected value of the key or index.
        inside:(List[str]) list of values that the key or index must be inside.
        not_inside:(List[str]) list of values that the key or index must not be inside.
        required:(bool) if the key or index is required.
        convert:(bool) if the key or index must be converted to str.
        default:(str) default value if the key or index is not required.
        max_len:(int) max length of the key or index.
        min_len:(int) min length of the key or index.
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
    max_len:int=None,
    min_len:int=None
)-> list:
    """This function is used to treat and get a list from a dict or list.
    Args:
        data:(dict or list) data to be treated.
        key_or_index:(int or str) key or index to be treated.
        expected_value:(list) expected value of the key or index.
        inside:(List[list]) list of values that the key or index must be inside.
        not_inside:(List[list]) list of values that the key or index must not be inside.
        required:(bool) if the key or index is required.
        default:(list) default value if the key or index is not required.
        max_len:(int) max length of the key or index.
        min_len:(int) min length of the key or index.    
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
    max:int=None,
    min:int=None
)-> int:
    """This function is used to treat and get a int from a dict or list.

    Args:
    
        data:(dict or list) data to be treated.
        key_or_index:(int or str) key or index to be treated.
        expected_value:(int) expected value of the key or index.
        inside:(List[int]) list of values that the key or index must be inside.
        not_inside:(List[int]) list of values that the key or index must not be inside.
        required:(bool) if the key or index is required.
        convert:(bool) if the key or index must be converted to int.
        default:(int) default value if the key or index is not required.
        max:(int) max value of the key or index.
        min:(int) min value of the key or index.
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
        max=max,
        min=min
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
    max:float=None,
    min:float=None
)-> float:
    """This function is used to treat and get a float from a dict or list.
    Args:
        data:(dict or list) data to be treated.
        key_or_index:(int or str) key or index to be treated.
        expected_value:(float) expected value of the key or index.
        inside:(List[float]) list of values that the key or index must be inside.
        not_inside:(List[float]) list of values that the key or index must not be inside.
        required:(bool) if the key or index is required.
        convert:(bool) if the key or index must be converted to float.
        default:(int) default value if the key or index is not required.
        max:(int) max value of the key or index.
        min:(int) min value of the key or index.
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
        max=max,
        min=min

    )


