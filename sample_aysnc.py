import aiohttp # 1, 
import asyncio # 2,

async def fetch(session, url): # 9,
    """非同期にURLからデータを取得する関数"""
    async with session.get(url) as response: # 10,
        return await response.text() # 11,

async def main():  # 5,
    """メインの非同期処理を行う関数"""
    async with aiohttp.ClientSession() as session:  # 6,
        url = "http://google.com"  # 7,
        html = await fetch(session, url) # 8,
        print(html) # 13,
        print('非同期処理の待機中！') # 12,

# asyncio.run()を使ってメイン関数を実行する
if __name__ == "__main__": # 3,
    asyncio.run(main()) # 4,

