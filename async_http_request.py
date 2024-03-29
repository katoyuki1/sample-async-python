import datetime
import aiohttp
import asyncio

start = datetime.datetime.now()

def log(message):
    print(f'{(datetime.datetime.now() - start).seconds}秒経過', message)

async def fetch(session, url):
    """非同期にURLからデータを取得する関数"""
    print(f"Fetching {url}")
    async with session.get(url) as response:
        return await response.text()

async def main():
    log("タスク開始")
    """メインの非同期処理を行う関数"""
    urls = [
        "http://google.com",
        "http://qiita.com",
        "https://www.python.org/",
        "https://www.mozilla.org/en-US/",
        "https://html.spec.whatwg.org/multipage/",
        "https://www.w3.org/TR/css/",
        "https://ecma-international.org/",
        "https://www.typescriptlang.org/",
        "https://www.oracle.com/jp/java/technologies/",
        "https://www.ruby-lang.org/ja/",
        "https://www.postgresql.org/",
        "https://www.mysql.com/jp/",
        "https://docs.djangoproject.com/ja/5.0/",
        "https://spring.pleiades.io/projects/spring-boot",
        "https://rubyonrails.org/"
        "https://firebase.google.com/?hl=ja",
        "https://go.dev/",
        "https://nodejs.org/en"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        
        print("Starting tasks...")
        # 非同期タスクを開始する前にメッセージを出力
        print("Tasks are running in the background...")
        
        # 非同期タスクの結果を待つ
        results = await asyncio.gather(*tasks)
        
        print("Tasks completed. Results:")
        for result in results:
            print(result[:100])  # 結果の最初の100文字を表示
    
    log("タスク終了")

# asyncio.run()を使ってメイン関数を実行する
if __name__ == "__main__":
    asyncio.run(main())
