from typing import Union,Any,Callable


def treat_and_get_all(data: Union[dict,list],callable:Callable):
    """
    Iterate over a dict or list and call a callable for each element
    Args:
        data (Union[dict,list]): dict or list to iterate
        callable (Callable): callable to call for each element
    """
    if isinstance(data,dict):
        for key in data:
            callable(data,key)

    elif isinstance(data,list):
        for index in range(len(data)):
            callable(data,index)