from asyncio import new_event_loop
from unittest import TestCase
from deasync import deasync_loop


class DeasyncTests(TestCase):
    def test_deasync_loop_fails_on_loop_none(self):
        with self.assertRaises(ValueError):
            @deasync_loop(loop=None)
            async def coroutine_with_loop(loop=None):
                return 42

    def test_deasync_loop_passes_loop(self):
        loop_set = None
        loop = new_event_loop()

        @deasync_loop(loop)
        async def coroutine_with_loop(loop=None):
            nonlocal loop_set
            loop_set = loop
            return 42

        result = coroutine_with_loop()

        self.assertEquals(loop, loop_set)
        self.assertEquals(42, result)

    def test_deasync_loop_does_not_pass_loop_if_not_accepted(self):
        loop_set = None
        loop = new_event_loop()

        @deasync_loop(loop)
        async def coroutine_with_loop():
            return 42

        result = coroutine_with_loop()

        self.assertEquals(loop_set, None)
        self.assertEquals(42, result)
