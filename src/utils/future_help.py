# -*- coding: utf-8 -*-
import functools
from concurrent.futures import thread

executor_pool = thread.ThreadPoolExecutor()


def run_on_executor(fn):
    """
    Decorator to run a synchronous method asynchronously
    """

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        future = executor_pool.submit(fn, *args, **kwargs)
        return future

    return wrapper
