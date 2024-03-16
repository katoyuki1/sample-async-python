import aiohttp
import asyncio

async def fetch(session, url):
    """非同期にURLからデータを取得する関数"""
    print(f"Fetching {url}")
    async with session.get(url) as response:
        return await response.text()

async def main():
    """メインの非同期処理を行う関数"""
    urls = [
        "http://google.com",
        "http://qiita.com",
        "https://www.python.org/"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        
        print("Starting tasks...")
        # 非同期タスクを開始する前にメッセージを出力
        await asyncio.sleep(2)  # 疑似的な待ち時間を作り出す
        print("Tasks are running in the background...")
        
        # 非同期タスクの結果を待つ
        results = await asyncio.gather(*tasks)
        
        print("Tasks completed. Results:")
        for result in results:
            print(result[:100])  # 結果の最初の100文字を表示

# asyncio.run()を使ってメイン関数を実行する
if __name__ == "__main__":
    asyncio.run(main())
