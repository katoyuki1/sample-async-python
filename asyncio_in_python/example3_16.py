import asyncio
import time

async def main(f: asyncio.Future):
  print(time.ctime())
  await asyncio.sleep(3)
  f.set_result('終わった！')
  print(time.ctime())

loop = asyncio.get_event_loop()
fut = asyncio.Future()
print(fut.done())# False

print(loop.create_task(main(fut)))

print(loop.run_until_complete(fut))# 終わった
print(fut.done())# True
print(fut.result())# 終わった