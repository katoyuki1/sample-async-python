import asyncio

async def say_after(delay, what):
  await asyncio.sleep(delay)
  print(what)

async def main():
  print("開始:", asyncio.get_running_loop().time())
  await say_after(1, "Yahoooo AsyncIO!")
  await say_after(2, 'goooood AsyncIO!')

  print("終わりだぁぁぁ！！:", asyncio.get_running_loop().time())

asyncio.run(main())