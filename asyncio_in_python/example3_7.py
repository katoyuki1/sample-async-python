import asyncio
import time

async def f():
  await asyncio.sleep(3.0)
  return 555

async def main():
  print(time.ctime())
  result = await f() # produce coroutine
  print(result)
  print(time.ctime())

asyncio.run(main())

