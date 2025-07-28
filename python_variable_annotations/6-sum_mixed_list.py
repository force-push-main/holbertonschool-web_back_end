#!/usr/bin/env python3

"""function with typed anotations"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]):
    return sum(mxd_lst)
