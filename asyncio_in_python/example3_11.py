import asyncio
import time
async def f():
  print(time.ctime())
  await asyncio.sleep(0)
  print(555)
  print(time.ctime())

loop = asyncio.get_event_loop()
coro = f()
loop.run_until_complete(coro)
