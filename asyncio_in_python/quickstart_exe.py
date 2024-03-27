import time
import asyncio

async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(3.0)
    print(f'{time.ctime()} Goodbye!')

def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} Hello from a thread!")

loop = asyncio.get_event_loop()
task = loop.create_task(main())

#イベントループの実行者（executor）を使用して、同期関数blocking()を実行します。Noneはデフォルトの実行者を使用することを意味します。
loop.run_in_executor(None, blocking)
#イベントループを開始し、task（main()関数のタスク）が完了するまで実行します
loop.run_until_complete(task)

#実行中のすべての非同期タスクを取得します。
pending = asyncio.all_tasks(loop=loop)
#取得したすべてのタスクをキャンセルします。
for task in pending:
    task.cancel()
#キャンセルされたタスクを集約し、例外を返す代わりに収集します。
group = asyncio.gather(*pending, return_exceptions=True)
#イベントループを再開し、groupの処理が完了するまで実行します。
loop.run_until_complete(group)
#イベントループを閉じて、プログラムの実行を終了します。イベントループを閉じることで、プログラムが使用していたリソースを適切に解放し、プログラムがきちんと終了するのを確実にします。
loop.close()

'''
このコードの流れを簡単にまとめると、次のようになります：

1. mainという非同期関数を定義して、最初に"Hello!"を出力し、3秒待ってから"Goodbye!"を出力します。

2. blockingという同期関数（ブロッキング関数）を定義して、2秒間待ってから"Hello from a thread!"を出力します。

3. イベントループを取得し、main関数を非同期タスクとしてイベントループに登録します。

4. 同期関数blockingを非同期的に実行します。

5. main関数が完了するまでイベントループを実行します。

6. 実行中のすべてのタスクを取得し、キャンセルします。

7. キャンセルされたタスクを集約して処理し、イベントループを再度実行します。
8. 最後に、イベントループを閉じてプログラムを終了します。


このコードは、非同期プログラミングの基本的なパターンを示しており、非同期タスクと同期関数がどのように組み合わせて使用されるかを理解するのに役立ちます。
また、イベントループの管理、タスクのキャンセル、例外の取り扱いなど、asyncioを使った非同期プログラミングのさまざまな側面を示しています。
'''