import asyncio

async def f():
  await asyncio.sleep(3.0)
  return 555

async def main():
  result = await f() # produce coroutine
  return print(result)

coro = f()
coro.send(None)
coro.throw(Exception, 'blah')