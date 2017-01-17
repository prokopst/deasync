from unittest import TestCase
from unittest.mock import Mock

from deasync import deasync


class DeasyncTests(TestCase):
    def test_deasync_loop_passes_loop(self):
        loop_set = None

        @deasync
        async def coroutine_with_loop(loop=None):
            nonlocal loop_set
            loop_set = loop
            return 42

        mock = Mock()
        result = coroutine_with_loop(loop=mock)

        self.assertEquals(mock, loop_set)
        self.assertEquals(42, result)

    def test_deasync_loop_does_not_pass_loop_if_not_accepted(self):
        loop_set = None

        @deasync
        async def coroutine_with_loop():
            return 42

        mock = Mock()
        result = coroutine_with_loop(loop=mock)

        self.assertEquals(mock, loop_set)
        self.assertEquals(42, result)
