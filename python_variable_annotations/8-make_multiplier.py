#!/usr/bin/env python3

"""type annotated function that returns function"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """function that returns a fucntion"""

    def callback(a_float: float):
        return a_float * multiplier
    return callback
