#!/usr/bin/env python3
'''write an async routine called wait_n
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return the list of all the delays
    '''
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
