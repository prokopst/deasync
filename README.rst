deasync provides a decorator called `deasync` for Python 3.5 (or higher) to make async functions synchronous in places where only synchronous functions are expected, for example in `unittest.TestCase`:

.. code:: python

    from asyncio import sleep
    from unittest import TestCase
    from deasync import deasync


    async def function42():
        await sleep(0.001)
        return 42


    class TestFunction42(TestCase):
        @deasync
        async def test_function42(self):
            result = await function42()
            self.assertEquals(42, result)
