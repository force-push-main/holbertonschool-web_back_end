#!/usr/bin/env python3

"""func that returns a asycio.task"""

import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> typing.Awaitable:
    """func that returns asyncio task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
