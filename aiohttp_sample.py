import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status) # レスポンスの結果の数値（ステータス）を出力
            print("Content-type:", response.headers['content-type']) # レスポンスのContent-typeを出力

            html = await response.text()
            print("Body:", html[:15], "...") # 取得した画面のhtmlコードを最初１５文字を出力

# main関数を非同期処理で実行。asyncio.run()で実行しないと、「RuntimeWarning: coroutine 'main' was never awaited」とエラーになる
asyncio.run(main()) 