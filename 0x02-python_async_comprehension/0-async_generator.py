#!/usr/bin/env python3
"""asynchronous coroutine 'async_generator'"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous coroutine that yields random numbers between 0
    and 10 after waiting 1 second asynchronously.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
