import asyncio
import time


def sync_blocking_operations():
    time.sleep(2)
    return "Operation completed"


async def run_sync_in_thread_pool():
    #現在実行中のイベントループを取得します。イベントループは、非同期操作をスケジュールし、実行するための中心的なメカニズムです。
    loop = asyncio.get_running_loop()
    #loop.run_in_executor(None, sync_blocking_operations)を使用して、sync_blocking_operations関数をデフォルトのスレッドプールエグゼキュータで実行します。
    #これにより、ブロッキング操作が非同期処理として実行され、メインスレッド（またはイベントループ）のブロッキングを回避できます。awaitにより、この操作の完了を非同期に待ちます。
    result = await loop.run_in_executor(None, sync_blocking_operations)
    print(result)


async def main():
    await run_sync_in_thread_pool()


asyncio.run(main())