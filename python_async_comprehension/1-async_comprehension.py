#!/usr/bin/env python3

"""async list comprehension"""

import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """async list comprehension"""
    return [value async for value in async_generator()]
