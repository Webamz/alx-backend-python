#!/usr/bin/env python3
"""asynchronous coroutine 'measure_runtime'"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime for executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension())

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
