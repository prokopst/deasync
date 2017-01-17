# deasync

Deasync provides a decorator called 'deasync' to make async functions/methods synchronous in places where synchronous functions are expected, for example in unittest.TestCase:

    from asyncio import sleep
    from unittest import TestCase
    from deasync import deasync
    
    
    async def function42():
        await sleep(0.001)
        return 42
    

    class TestFunction42(TestCase):
        @deasync
        def test_function42(self):
            result = await function42()
            self.assertEquals(42, result)

License MIT.
