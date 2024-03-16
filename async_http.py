import asyncio
import aiohttp

async def fetch(session, url):
    """非同期にURLからデータを取得する関数"""
    async with session.get(url) as response:
        return await response.text(), response.status

async def main():
    """メインの非同期処理を行う関数"""
    urls = [
        "http://google.com",
        "http://qiita.com",
        "https://www.python.org/"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        
        for response in responses:
            print(response)

# asyncio.run()を使ってメイン関数を実行する
if __name__ == "__main__":
    asyncio.run(main())

'''
【コード解説】
・import asyncio: 
asyncioライブラリをインポートします。
asyncioはPythonの標準ライブラリで、非同期プログラミングをサポートします。
非同期プログラミングとは、プログラムが一度に複数の操作を実行できるようにすることです。

・import aiohttp: 
aiohttpライブラリをインポートします。
aiohttpはHTTPクライアント/サーバーのための非同期フレームワークです。
これを使って、Webサイトからデータを非同期に取得することができます。

・async def fetch(session, url): 
非同期関数fetchを定義します。
この関数はsession（Webサイトとの通信セッションを管理するオブジェクト）とurl（データを取得したいWebサイトのアドレス）を引数に取ります。

・async with session.get(url) as response: 
指定されたurlに非同期でGETリクエストを送り、そのレスポンス（返答）を変数responseに格納します。
async withは非同期処理を行う際に使用されるキーワードで、操作が完了するまで次の行のコードの実行を待ちます。

・return await response.text(), response.status: 
レスポンスの本文を非同期に読み取り、そのテキストとステータスコード（HTTPリクエストの結果を示す数字）を返します。

・async def main(): 
プログラムのメイン処理を行う非同期関数mainを定義します。

・urls = [...: 
データを取得したいURLのリストを定義します。

・async with aiohttp.ClientSession() as session: 
aiohttpを使用してHTTP通信のためのセッションを開始します。
このセッションを通じて、Webサイトにリクエストを送信します。

・tasks = [fetch(session, url) for url in urls]: 
各URLに対してfetch関数を呼び出すタスクのリストを作成します。
これにより、複数のWebサイトから同時にデータを取得する準備が整います。

・responses = await asyncio.gather(*tasks): 
asyncio.gatherを使用して、先ほど作成した全てのタスクを同時に実行します。
awaitはこれらのタスクが全て完了するまでプログラムの実行を一時停止します。

・for response in responses: print(response): 
各リクエストのレスポンスをループで処理し、コンソールに出力します。

・if __name__ == "__main__": asyncio.run(main()): 
スクリプトが直接実行された場合にのみ、main関数を非同期で実行します。これはプログラムのエントリーポイント（開始点）です。
Pythonでif __name__ == "__main__":という条件文を書く理由は、
スクリプトが直接実行された場合のみ、特定のコードブロックを実行するようにするためです。
この機能を使うことで、スクリプトが他のファイルによってモジュールとしてインポートされた時と、直接実行された時とで、スクリプトの振る舞いを変えることができます。

Pythonにおいて、__name__は現在のファイルの名前を表す組み込み変数です。
もしファイルが直接実行されている場合、__name__の値は"__main__"になります。
一方、ファイルが他のファイルからインポートされている場合（つまり、モジュールとして使用されている場合）、__name__はそのファイル名（拡張子.pyなし）になります。

この機能を利用することで、ファイルがスクリプトとして実行された時にのみ実行したい処理（例えば、テストコードやデモ用のコード）を
if __name__ == "__main__":の下に記述することができます。
これにより、他のファイルからこのファイルをインポートしても、インポートした側で不要なコードが実行されることを防げます。
'''
