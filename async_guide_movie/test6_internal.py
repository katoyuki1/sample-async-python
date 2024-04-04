'''
簡易的なタスクスケジューラーを実装。非同期コルーチンを特定の遅延後に実行するためのもの
heapqを使用することで、タスクの実行順序を効率的に管理
'''
import asyncio
import time
import heapq #ヒープキュー（優先度キュー）を扱うためのもの

#タスクをスケジュールし、指定された遅延後に実行する役割
class SimpleTaskScheduler:
    def __init__(self):
        #コンストラクタで、実行するタスクを保持するリストtasksを初期化
        self.tasks = []

    #coroは実行するコルーチン、delayはそのコルーチンをいつ実行するかの遅延時間（秒）
    def add_task(self, coro, delay):
        #現在時刻に遅延時間を加えた実行時刻を計算し、それとコルーチンを、タプルとしてタスクリストに追加
        exec_time = time.time() + delay
        #実行時刻の早い順にタスクが並べる
        heapq.heappush(self.tasks, (exec_time, coro))

    async def run(self):
        #タスクリストが空になるまでループ
        while self.tasks:
            #タスクリストから実行時刻が最も早いタスクを取り出す
            exec_time, coro = heapq.heappop(self.tasks)
            #現在時刻がタスクの実行時刻よりも前であれば、実行時刻までスリープ
            now = time.time()
            if now < exec_time:
                await asyncio.sleep(exec_time - now)

            #タスク（コルーチン）を実行。例外が発生した場合は、その情報を出力
            try:
                print(f"Executing {coro.__name__} at {time.time()}")
                await coro()
            except Exception as e:
                print(f"Task {coro.__name__} raised {e}")


async def sample_task():
    print(f"Task executed at {time.time()}")


async def main():
    scheduler = SimpleTaskScheduler()
    scheduler.add_task(sample_task, 3)
    scheduler.add_task(sample_task, 1)

    await scheduler.run()

asyncio.run(main())