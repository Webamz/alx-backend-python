#!/usr/bin/env python3
"""asynchronous coroutine 'async_comprehension'"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers
    using async comprehension over async_generator.

    Returns:
        List[float]: List of 10 random numbers.
    """
    random_numbers = [
            random_number async for random_number in async_generator()]
    return random_numbers
