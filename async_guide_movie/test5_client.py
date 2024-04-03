'''このコードはPythonで非同期プログラミングを利用して、TCPエコークライアントを実装した例です。
クライアントはメッセージをサーバーに送信し、サーバーからの応答を受け取り、接続を閉じます。
'''
import asyncio

#この関数は、サーバーに送信するメッセージを引数として受け取ります。asyncキーワードは、この関数が非同期であることを示します。
async def tcp_echo_client(message):
    #指定されたIPアドレス("127.0.0.1")とポート番号(5003)でTCP接続を非同期に開きます。awaitキーワードは、接続が完了するまで待つことを示します。
    #readerとwriterは、接続を通じてデータを読み書きするために使用されるオブジェクトです。
    reader, writer = await asyncio.open_connection("127.0.0.1", 5003)
    print(f"Send {message}")
    #メッセージをUTF-8でエンコードし、サーバーに送信します。writeメソッドは、バイト列を引数として受け取ります。
    writer.write(message.encode('utf8'))

    #サーバーから最大100バイトのデータを非同期に読み込みます。読み込まれるまでプログラムの実行は待機されます
    data = await reader.read(100)
    #受信したデータをUTF-8でデコードし、コンソールに表示します。
    print(f"Received {data.decode('utf8')}")
    print("Close the connection")

    #writerオブジェクトのcloseメソッドを呼び出して、TCP接続を閉じます。
    writer.close()
    #接続が完全に閉じられるまで待ちます。awaitキーワードは、その完了を非同期に待つことを示します
    await writer.wait_closed()


asyncio.run(tcp_echo_client("Cooooool !"))