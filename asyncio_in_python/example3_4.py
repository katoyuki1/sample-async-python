import asyncio
import inspect

async def f():
  return 123

def g():
  return 456

print(type(f))
print(type(g))

print(inspect.iscoroutinefunction(f))
print(inspect.iscoroutinefunction(g))