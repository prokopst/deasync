from asyncio import coroutine, iscoroutinefunction, get_event_loop
from unittest import TestCase
from deasync import deasync, deasync_loop
import itertools


async def new_style_async_coroutine(num):
    return num + 42


@coroutine
def old_style_async_coroutine(num):
    yield
    return num + 42


class DeasyncTests(TestCase):
    deasync_functions = [deasync, deasync_loop(loop=get_event_loop())]
    coroutines = [new_style_async_coroutine, old_style_async_coroutine]

    def test_deasync_fails_for_noncoroutine(self):
        for deasync_function in self.deasync_functions:
            with self.subTest(deasync=deasync_function.__name__):
                with self.assertRaises(ValueError):
                    @deasync_function
                    def normal_function():
                        pass

    def test_deasync_creates_function_from_coroutine(self):
        for deasync_function, coro in itertools.product(self.deasync_functions, self.coroutines):

            with self.subTest(deasync=deasync_function.__name__, coroutine=coro.__name__):
                self.assertTrue(iscoroutinefunction(coro))
                deasync_coro = deasync(coro)
                self.assertFalse(iscoroutinefunction(deasync_coro))

                value = deasync_coro(100)
                self.assertEquals(value, 142)
