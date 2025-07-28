#!/usr/bin/env python3

"""type annotated func that returns total runtime"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """aforementioned annotated function"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return ((end_time - start_time) / n)
