import asyncio
async def f():
  try:
    while True: await asyncio.sleep(0)
  except asyncio.CancelledError:
    print('キャンセルだ！')
  else:
    return print(555)

coro = f()
coro.send(None)
coro.send(None)
coro.throw(asyncio.CancelledError)