'''
Pythonの非同期I/Oライブラリであるasyncioと、SQLiteデータベース非同期操作ライブラリであるaiosqliteを使って、データベースの操作を非同期に行う
'''
import asyncio
import aiosqlite


async def create_table(db_name, table_name):
    #非同期にデータベースに接続し、その接続をdbとして扱います。
    #async with文は、非同期操作のコンテキスト管理に使われ、このブロックが終了すると自動的に接続が閉じられます。
    async with aiosqlite.connect(db_name) as db:
        #SQL文を実行してテーブルを作成します。このテーブルにはid（整数型、主キー）とmessage（テキスト型）の2つのカラムがあります。
        #if not existsは、同名のテーブルが存在しない場合にのみテーブルを作成します。awaitキーワードは、非同期操作が完了するまで待機することを示します。
        await db.execute(f'Create table if not exists {table_name} (id integer primary key, message text)')
        await db.commit()


async def insert_data(db_name, table_name, message):
    async with aiosqlite.connect(db_name) as db:
        #テーブルにデータを挿入するSQL文を実行します。
        #プレースホルダ?は、SQLインジェクション攻撃を防ぐために使用されます。この場合、messageの内容がプレースホルダに代入されます。
        await db.execute(f'insert into {table_name} (message) VALUES (?)', (message,))
        await db.commit()

#この関数は、データベースとテーブル名を引数として受け取り、テーブルの内容を取得します。
async def fetch_data(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        #指定されたテーブルからidとmessageを選択するSQLクエリを実行し、結果を非同期に取得します。
        async with  db.execute(f'SELECT id,message FROM {table_name}') as cursor:
            #結果はリストとして返されます。
            return [row async for row in cursor]


async def main():
    #指定したデータベースとテーブルでテーブルを作成し、データを挿入して、挿入したデータを取得します。
    db_name = 'test.db'
    table_name = 'greetings'
    await create_table(db_name=db_name, table_name=table_name)
    await insert_data(db_name=db_name, table_name=table_name, message="Hello, AsyncIO!")
    greetings = await fetch_data(db_name=db_name, table_name=table_name)
    #取得したデータをコンソールに表示します。
    for greeting in greetings:
        print(f"Greeting {greeting[0]}: {greeting[1]}")


asyncio.run(main())