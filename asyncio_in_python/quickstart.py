import asyncio, time

async def main():
  # 現在の時刻と"Hello!"の文字列を出力します。time.ctime()は現在の時刻を文字列で返します
  print(f'{time.ctime()} Help!Async is difficult!')
  # await式を使用してasyncio.sleep(2.0)を呼び出し、非同期に2秒間プログラムの実行を停止します。この間、イベントループは他のタスクを実行することができます
  await asyncio.sleep(2.0)
  # 2秒の待機後、再び現在の時刻と"Goodbye!"の文字列を出力します
  print(f'{time.ctime()} I understand!')

#asyncio.run()関数を使ってmain()関数をイベントループで実行します。これは、Python 3.7以降で導入された新しい実行方法です。この行がプログラムのエントリーポイントとなり、main()関数内の非同期処理が実行されます。
asyncio.run(main())