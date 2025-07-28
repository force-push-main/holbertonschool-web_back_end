#!/usr/bin/env python3

"""async function that returns delay"""

import random
import asyncio


async def wait_random(max_delay):
    """asyn func that returns random float"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
