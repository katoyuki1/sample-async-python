'''
このコードを実行すると、プログラムの開始時刻、Hanakoへの挨拶（1秒後）、Taroへの挨拶（さらに1秒後、合計2秒後）
非同期で行なっているため1+2=3秒ではなく、2秒で完了している。
'''
import asyncio
import time

async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"hello {name}, after {delay} seconds!")

async def main():
    #HanakoとTaroに対して、それぞれ1秒と2秒の遅延でgreet関数を非同期タスクとして実行します。asyncio.create_taskを使用して、これらのタスクを作成します。
    task1 = asyncio.create_task(greet("Hanako", 1))
    task2 = asyncio.create_task(greet("Taro", 2))

    await task1
    await task2


print(time.ctime())
asyncio.run(main())
print(time.ctime())

'''
非同期タスクとは、プログラムの主な実行フローをブロックすることなくバックグラウンドで実行される処理のことを指します。
一般的に、非同期タスクは入出力操作（ネットワーク通信、ディスクへの読み書きなど）や時間がかかる計算など、完了に時間がかかる可能性がある作業に対して使用されます。

create_taskをする意味は、指定された非同期関数（この場合はgreet関数）を非同期タスクとしてスケジュールし、それがバックグラウンドで実行されるようにすることです。
これにより、その関数の実行がメインのプログラムの流れを妨げることなく進行します。
具体的には、プログラムはgreet関数の実行を待たずに次の行のコードに進むことができ、複数のgreet関数を並行して実行することが可能になります。

このコンセプトの主な利点は、効率性と応答性の向上です。
例えば、greet関数が重いデータベースクエリや遅延のあるネットワークリクエストを行う場合でも、その関数が結果を返すのをメインのプログラムが待つ必要がありません。
その間に、プログラムは他のタスクを実行することができます。

asyncio.create_taskを使用して非同期タスクを作成することで、プログラマは明示的に非同期操作をスケジュールし、それらの操作がいつ完了するかを柔軟に制御できるようになります。
これにより、同時に複数の操作を効率的に実行し、アプリケーションのパフォーマンスを向上させることが可能です。

簡単に言うと、create_taskを使用することで、プログラムがスムーズに動作し続ける間に、複数の作業を同時にこなすことができるようになります。
これは特に、ウェブサーバーのように同時に多くのリクエストを処理する必要があるアプリケーションにおいて有用です。
'''