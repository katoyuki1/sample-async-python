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

# main() コルーチンをスケジュールし、future を渡します。
# main() コルーチンが行うことはスリープしてから Future インスタンスを切り替えることだけであることに注意。 (main() コルーチンはまだ実行を開始しないことに注意。コルーチンはループの実行中にのみ実行される。)
print(loop.create_task(main(fut)))

# ここでは、Task インスタンスではなく Future インスタンスで run_until_complete() を使用します。7 これは、これまでに見たものとは異なります。ループが実行されているので、main() コルーチンが実行を開始します。
print(loop.run_until_complete(fut))# 終わった
print(fut.done())# True
print(fut.result())# 終わった