import asyncio

#クライアントからの接続を非同期に処理する関数.readerとwriterオブジェクトは、クライアントとのデータの読み書きに使用
async def handle_client(reader, writer):
    #クライアントから最大100バイトのデータを非同期に読み込みます。awaitは非同期処理の完了を待つために使用されます。
    data = await reader.read(100)
    #読み込まれたデータ（バイト列）をUTF-8でデコードし、文字列に変換します
    message = data.decode('utf8')
    #クライアントのアドレス情報を取得します。get_extra_info('peername')は、接続されたクライアントのリモートアドレスを返します
    addr = writer.get_extra_info('peername')

    print(f"received {message} from {addr}")
    #クライアントに"ack"（acknowledgement、受信確認）を送信することを表示
    print("sending ack")
    #"ack"をUTF-8でエンコードし、クライアントに送信
    writer.write("ack".encode('utf8'))
    #送信バッファが空になるまで、つまりすべての送信データがクライアントに送り出されるまで待ちます
    await writer.drain()
    #通信を終了するために、writerストリームを閉じます
    writer.close()


async def main():
    #指定されたアドレス('127.0.0.1')とポート(5003)で非同期サーバーを起動します。handle_client関数は、クライアントからの各接続に対して呼び出されます
    server = await asyncio.start_server(handle_client, '127.0.0.1', 5003)
    #サーバーが実際にバインドされているアドレスとポートを取得します
    addr = server.sockets[0].getsockname()

    #async with文を使用して、サーバーがクライアントからの接続を無限に待ち受けるようにします。
    async with server:
        await server.serve_forever()


asyncio.run(main())