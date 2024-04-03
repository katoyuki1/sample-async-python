'''
Pythonで非同期I/Oを利用してPostgreSQLデータベースとのやり取りを行う
'''
import asyncio
import aiopg
from dotenv import load_dotenv #dotenvは環境変数を.envファイルから読み込むためのモジュール
import os #環境変数にアクセスするためのモジュール

# 環境変数をロード
load_dotenv()

# 環境変数から設定を読み込む
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')

# 読み込んだ接続情報を使ってDSN（Data Source Name）文字列を構築します。この文字列は、aiopgでデータベースに接続する際に使用します。
dsn = f'dbname={db_name} user={db_user} password={db_password} host={db_host}'

async def create_table(table_name):
    #DSNを使って非同期にデータベース接続プールを作成し、poolとして利用します。このプールを通じて、複数のデータベース接続を効率的に管理します。
    async with aiopg.create_pool(dsn) as pool:
        #プールから非同期にデータベース接続を取得し、connとして利用します。
        async with pool.acquire() as conn:
            #データベース接続からカーソルを非同期に取得し、curとして利用します。カーソルはSQLコマンドを実行するために使用します。
            async with conn.cursor() as cur:
                #SQLコマンドを非同期に実行し、指定されたテーブル名でテーブルが存在しない場合に新しく作成します。このテーブルにはidとmessageの2つのカラムが含まれます。
                await cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, message TEXT)')
                #await conn.commit() aiopgは自動的にトランザクションをコミットするためコメントアウト

async def insert_data(table_name, message):
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f'INSERT INTO {table_name} (message) VALUES (%s)', (message,))
                #await conn.commit()

async def fetch_data(table_name):
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(f'SELECT id, message FROM {table_name}')
                return [row async for row in cur]

async def main():
    table_name = 'greetings'
    await create_table(table_name=table_name)
    await insert_data(table_name=table_name, message="Hello, AsyncIO with PostgreSQL!")
    greetings = await fetch_data(table_name=table_name)
    for greeting in greetings:
        print(f"Greeting {greeting[0]}: {greeting[1]}")

asyncio.run(main())
