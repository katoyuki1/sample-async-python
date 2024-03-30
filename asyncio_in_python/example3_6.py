async def f():
  return 123

coro = f()
try:
   # コルーチンの開始。コルーチンとは非同期処理を可能にするオブジェクト。実行を開始、停止し、後から再開できる
   # Noneを送信することで、コルーチンcoroの最初のyield式まで実行を進めます。ただし、この例ではyieldを使っていないため、単にコルーチンを開始しています
  coro.send(None)
except StopIteration as e:
  print('答えは・・・:', e.value) # コルーチンの終了
