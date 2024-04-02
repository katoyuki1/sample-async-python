# pip install fastapi uvicorn
'''fastapiはウェブアプリケーションフレームワークです。
uvicornはASGI（Asynchronous Server Gateway Interface）サーバーで、FastAPIアプリケーションを実行するために使用されます。
'''

from fastapi import FastAPI
import uvicorn # uvicornモジュールをインポートします。これを使用して、アプリケーションを起動し、外部からのリクエストを受け取れるようにします。
import asyncio

app = FastAPI() # FastAPIクラスのインスタンスを作成し、appという変数に代入します。このインスタンスがウェブアプリケーションの中心となります。

@app.get('/')#デコレータを使用してルートエンドポイント（'/'）を定義します。このエンドポイントはHTTP GETリクエストを受け取ります。
async def read_root():#非同期関数read_rootを定義します。この関数はルートエンドポイントに対するリクエストを処理します。
    return {"Hello": "World"}#JSON形式のレスポンスを返します。この例では、単純な辞書を返していますが、FastAPIが自動的にJSONに変換します


@app.get('/items/{item_id}')#/items/{item_id}パスのエンドポイントを定義します。{item_id}はパスパラメータで、URLから値を取得するために使用されます。
async def read_item(item_id: int):#item_idパラメータを受け取り、非同期関数read_itemを定義します。この関数は/items/{item_id}エンドポイントに対するリクエストを処理します。
    await asyncio.sleep(1)#非同期に1秒間待機
    return {"item_id": item_id, "name": f"Item {item_id}"}#JSON形式のレスポンスを返します。ここでは、受け取ったitem_idを使用してレスポンスを作成


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)#、FastAPIアプリケーションを起動します。host="127.0.0.1"とport=8000で、アプリケーションがローカルマシンの8000ポートでリクエストを待ち受けるように指定しています。