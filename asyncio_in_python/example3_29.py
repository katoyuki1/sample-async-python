import asyncio

async def f(delay):
    await asyncio.sleep(delay)

loop = asyncio.get_event_loop()
t1 = loop.create_task(f(1))  # タスク1は1秒間実行されます
t2 = loop.create_task(f(2))  # タスク2は2秒間実行されます
loop.run_until_complete(t1) # タスク1が完了するまで実行
loop.close() # イベントループを閉じる