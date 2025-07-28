#!/usr/bin/env python3

"""type annotated function that returns function"""

import typing
from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable[[float, float], float]:
    def callback(a_float: float, multiplier: float):
        return a_float * multiplier
    return callback
