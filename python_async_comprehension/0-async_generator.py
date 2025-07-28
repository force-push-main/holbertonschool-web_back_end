#!/usr/bin/env python3

"""async generator that yields random ints"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """function as described above"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
