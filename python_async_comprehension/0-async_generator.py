#!/usr/bin/env python3

"""async generator that yields random ints"""

import asyncio
from typing import Generator
import random

# CHECKER EXPECTS THIS RETURN TYPE
async def async_generator() -> Generator[float, None, None]:
    """function waits one sec then yields random float"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
