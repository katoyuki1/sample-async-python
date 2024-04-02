import asyncio

#この関数はチャットクライアントのメイン処理を担います。引数にはクライアント名、ホスト名、ポート番号
async def chat_client(name, host, port):
    #指定されたホストとポートで非同期に接続を開きます。readerはデータ読み込み用、writerはデータ書き込み用のオブジェクトです。
    reader, writer = await asyncio.open_connection(host,port)
    print(f"{name} connected to chat server {host}:{port}")

    #メッセージを非同期に送信するためのローカル非同期関数send_messagesを定義
    async def send_messages():
        #無限ループを使って、ユーザーがメッセージを入力し続けることができるようにします
        while True:
            #ユーザーからのメッセージ入力を待ちます。
            message = input(f"{name}: ")
            #入力されたメッセージをエンコードして、サーバーに送信します
            writer.write(message.encode())
            #メッセージの送信が完了するまで待機します。drainは送信バッファが空になるまで待つためのメソッドです。
            await writer.drain()

    #サーバーからのメッセージを非同期に受信するためのローカル非同期関数received_messagesを定義
    async def received_messages():
        #無限ループを使って、サーバーからのメッセージを常に受け取ることができるようにします
        while True:
            #サーバーから最大100バイトのデータを非同期に読み込みます
            data = await reader.read(100)
            #もしデータがなければ（サーバーからの切断を示している場合）、ループを抜けます
            if not data:
                #切断メッセージを表示し、書き込み用のオブジェクトを閉じます
                print("Disconnected from chat server")
                writer.close()
                break
            #サーバーから読み込んだデータをデコードし、出力
            print(data.decode())

    #メッセージ送信と受信処理をそれぞれ非同期タスクとして作成します。
    send_task = asyncio.create_task(send_messages())
    receive_task = asyncio.create_task(received_messages())
    #送信タスクと受信タスクが完了するまで待機します。これにより、両方の非同期処理が平行して実行されます。
    await asyncio.gather(send_task,receive_task)

if __name__ == '__main__':
    #ユーザーに名前の入力を促します。
    name = input("Enter your name: ")
    #chat_client関数を非同期に実行し、チャットクライアントを開始します。ここではlocalhostとポート5003を使用しています。
    asyncio.run(chat_client(name,"localhost",5003))