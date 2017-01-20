# deasync

[![Pypi version](https://img.shields.io/pypi/v/deasync.svg)](https://pypi.python.org/pypi/deasync) [![Run Status](https://api.shippable.com/projects/587b90e6e69a190f0021e846/badge?branch=master)](https://app.shippable.com/projects/587b90e6e69a190f0021e846) [![Coverage Badge](https://api.shippable.com/projects/587b90e6e69a190f0021e846/coverageBadge?branch=master)](https://app.shippable.com/projects/587b90e6e69a190f0021e846)

deasync provides a decorator called `deasync` for Python 3.5 (or higher) to make async functions synchronous in places where only synchronous functions are expected, for example in `unittest.TestCase`:

```python
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
```
