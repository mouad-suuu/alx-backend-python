#!/usr/bin/env python3
'''Given the parameters and the return values,
add type annotations to the function
Hint: look into TypeVar
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
'''
from typing import Mapping, Any, Union, TypeVar


res = Union[Any, None]
df = Union[Any, None]


def safe_get_value(dct: Mapping, key: Any, default: df = None) -> res:
    ''' Returns the value of a key in a dictionary if it exists,
    otherwise None. '''
    if key in dct:
        return dct[key]
    else:
        return default
