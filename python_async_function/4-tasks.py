#!/usr/bin/env python3

"""func gathers async funcs and returns in delay order"""

import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """async func that does as stated above"""
    async_funcs = [wait_random(max_delay) for _ in range(n)]
    results = []
    for func in asyncio.as_completed(async_funcs):
        result = await func
        results.append(result)
    return results
