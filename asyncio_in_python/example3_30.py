import asyncio
from asyncio import StreamReader, StreamWriter

async def echo(reader: StreamReader, writer: StreamWriter):#非同期関数echoを定義しています。この関数は、接続ごとにStreamReaderオブジェクトとStreamWriterオブジェクトを引数として受け取ります
  print('New connection')
  try:
    while data := await reader.readline():#クライアントからのデータを一行ずつ非同期で読み込むループを開始します。Pythonの代入式（:=）を使用して、data変数に読み込んだ行を代入し、その行が空でない限りループを続けます
      writer.write(data.upper())#読み込んだデータを大文字に変換して、クライアントに送り返します。
      await writer.drain()#書き込み操作が完了するまでプログラムの実行を一時停止します。drain()メソッドは、バッファに書き込まれたデータを実際に送信することを保証します。
    print('Leaving Connection.')
  except asyncio.CancelledError:# タスクがキャンセルされた場合（例えばサーバーがシャットダウンする時）に発生するCancelledError例外をキャッチします。
    print('Connection dropped!')

async def main(host='127.0.0.1', port=8888):
  # echo関数をコールバックとして使用するTCPサーバーを起動します。
  server = await asyncio.start_server(echo, host, port)
  async with server: #非同期withステートメントを使用して、サーバーオブジェクトのコンテキストを管理します。これにより、サーバーが適切に開始され、後片付けも自動で行われます。
    await server.serve_forever() # サーバーが永久にリクエストを受け付けるようにします。このコマンドは、プログラムが明示的に停止されるまで終了しません。

try:
  asyncio.run(main())
except KeyboardInterrupt:
  print('Bye')