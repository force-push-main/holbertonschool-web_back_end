#!/usr/bin/env python3

"""func gathers async funcs and returns in delay order"""

import asyncio
import typing
wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> typing.Sequence[float]:
    """async func that does as stated above"""
    funcs = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*funcs)
    return results
