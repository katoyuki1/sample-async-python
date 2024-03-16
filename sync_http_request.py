import datetime
import requests

start = datetime.datetime.now()

def log(message):
    """ログを出力する関数"""
    print(f'{(datetime.datetime.now() - start).seconds}秒経過', message)

def fetch(url):
    """同期的にURLからデータを取得する関数"""
    print(f"Fetching {url}")
    response = requests.get(url)
    return response.text

def main():
    """メインの同期処理を行う関数"""
    log("タスク開始")
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
    
    print("Starting tasks...")
    # 同期的にHTTPリクエストを実行
    results = [fetch(url) for url in urls]
    
    print("Tasks completed. Results:")
    for result in results:
        print(result[:100])  # 結果の最初の100文字を表示
    
    log("タスク終了")

if __name__ == "__main__":
    main()
