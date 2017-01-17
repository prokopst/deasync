"""
deasync decorator is useful in a place where async functions/methods are not desired,
for example in unittest.TestCase.

.. code:: python

    from unittest import TestCase

    class TestMyAsyncMethod(TestCase):
        @deasync
        async def test_my_async_method(self):
            result = await my_async_method()
            self.assertEquals(result, True)


"""
from asyncio import get_event_loop, iscoroutinefunction
import inspect
from functools import wraps

__all__ = ['deasync', 'deasync_loop']


def _verify_is_coroutine(coro):
    if not iscoroutinefunction(coro):
        raise ValueError("function is not a coroutine function")


def _fix_old_style_coroutine(wrapper):
    """
    Handle "old style" coroutines defined with asyncio.coroutine decorator.
    """
    # "old-style" coroutines recognized by '_is_coroutine' attribute, no kidding
    is_coroutine = getattr(wrapper, '_is_coroutine', None)
    if is_coroutine is True:
        wrapper._is_coroutine = False


def deasync(function):
    """
    A decorator to make an async function synchronous.

    :param function: a coroutine function
    :type function: callable
    """
    _verify_is_coroutine(function)

    @wraps(function)
    def wrapper(*args, **kwargs):
        return get_event_loop().run_until_complete(function(*args, **kwargs))

    _fix_old_style_coroutine(wrapper)

    return wrapper


def deasync_loop(loop):
    """
    A decorator to make an async function synchronous. This is an extended version
    to support explicit loop and and passes the loop the the async function.

    :param loop: optional eventloop for those who loves it as an explicit parameter
    :type loop: asyncio.AbstractEventLoop
    """
    def deasync_loop_decorator(function):
        _verify_is_coroutine(function)

        if loop is None:
            raise ValueError("loop must be set")

        function_signature = inspect.signature(function)

        if 'loop' in function_signature.parameters:
            @wraps(function)
            def wrapper(*args, **kwargs):
                return loop.run_until_complete(function(loop=loop, *args, **kwargs))
        else:
            @wraps(function)
            def wrapper(*args, **kwargs):
                return loop.run_until_complete(function(*args, **kwargs))

        _fix_old_style_coroutine(wrapper)

        return wrapper

    return deasync_loop_decorator
