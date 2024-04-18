#!/usr/bin/env python3
'''Annotate the below function’s parameters
and return values with the appropriate types
def element_length(lst):
    return [(i, len(i)) for i in lst]
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains a sequence and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
