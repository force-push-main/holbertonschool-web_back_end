#!/usr/bin/env python3

"""type annotated function that returns tuple"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """function that returns tuple"""

    return (k, v ** 2)
