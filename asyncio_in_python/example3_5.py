import inspect

async def f():
  return 123

coro = f()
print(type(coro))

print(inspect.iscoroutine(coro))