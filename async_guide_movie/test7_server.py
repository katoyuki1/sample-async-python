'''
このコードは、Pythonで書かれた非同期チャットサーバーの例です。
asyncioライブラリを使用しており、同時に複数のクライアントからの接続を受け付け、クライアント間でメッセージをやり取りできます
'''
import asyncio

#クラスは、データと機能（メソッド）を一つにまとめたものです。
class ChatServer:
    #クラスの初期化メソッドです。
    def __init__(self):
        #このチャットサーバーのクライアントを保持するためのリストself.clientsを初期化しています。
        self.clients = []

    #非同期メソッドhandle_clientを定義。このメソッドは、サーバーに接続された各クライアントを処理します。
    #readerとwriterは、クライアントとの通信に使われるオブジェクトです。
    async def handle_client(self, reader, writer):
        #現在のクライアント（writer）をクライアントリストに追加
        self.clients.append(writer)
        #クライアントのアドレス情報を取得
        addr = writer.get_extra_info('peername')
        print(f"New connection from {addr}")
        #無限ループを開始します。これにより、クライアントからのデータを継続的に受け取ることができます
        while True:
            #クライアントから最大100バイトのデータを非同期に読み取ります。awaitは、非同期操作が完了するまで待つことを示します
            data = await reader.read(100)
            #データがない場合（クライアントが接続を閉じた場合）、ループを抜けます
            if not data:
                #クライアントが接続を閉じたことを表示し、クライアントリストから削除し、書き込み用オブジェクトを閉じます。
                print(f"Connection closed by {addr}")
                self.clients.remove(writer)
                writer.close()
                break
            #受け取ったバイトデータをデコード（文字列に変換）します
            message = data.decode()
            print(f"Recived from {addr}: {message}")
            #クライアントリストをループし、各クライアントにメッセージを送信します
            for client in self.clients:
                #メッセージを送信したクライアント以外の全クライアントにメッセージを送ります
                if client != writer:
                    #データを送信し、drain()メソッドで送信が完了するのを待ちます
                    client.write(data)
                    await client.drain()
        print(f"End connection from {addr}")

    #サーバーを起動するための非同期メソッドです。指定されたホストとポートでサーバーを起動します
    async def run_Server(self, host, port):
        #指定されたホストとポートで非同期サーバーを起動し、クライアントからの接続を待ち受けます。
        server = await asyncio.start_server(self.handle_client, host, port)
        #サーバーのアドレス情報を取得します。
        addr = server.sockets[0].getsockname()
        #サーバーが起動しているアドレスとポートを表示します
        print(f"Serving on {addr}")

        #async with文を使用してサーバーを永続的に実行します。これにより、クライアントからの接続を無限に受け付け続けます。
        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    chat = ChatServer()
    #run_Serverメソッドを非同期に実行し、サーバーをlocalhostの5003ポートで起動します。
    asyncio.run(chat.run_Server("localhost", 5003))