'''
asyncioライブラリを使って複数の非同期タスクを同時に実行し、それらがすべて完了するのを待つ方法を示す
'''
import asyncio

async def async_task(name, delay):
    print(f"Task {name} started")
    #asyncio.sleep(delay)を使って、指定された秒数（delay）だけ非同期に処理を一時停止する。この関数は、遅延をシミュレートするため
    await asyncio.sleep(delay)
    print(f"Task {name} completed")
    return f"Task {name} done"
    
#プログラムのエントリーポイント(処理の開始場所)
async def main():
    #タスク名と遅延時間のタプルのリストを定義。このリストを使って、複数のタスクを作成
    names_and_delays = [("A", 1), ("B", 2), ("C", 3)]
    #リスト内包表記を使って、各タプルに対してasync_task関数の非同期タスクを作成し、tasksリストに格納する
    #asyncio.create_task()は非同期関数をタスクとしてスケジュールし、即座に実行を開始する
    tasks = [asyncio.create_task(async_task(name, delay)) for name, delay in names_and_delays]
    
    #asyncio.wait()を使って、tasksリストに含まれるすべてのタスクが完了するまで待つ。
    #return_when=asyncio.ALL_COMPLETEDは、全てのタスクが完了した時点で待機を解除することを指示する。
    completed, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    
    for completed_task in completed:
        #各完了したタスクの結果（return文で返された値）を表示する
        print(completed_task.result()) # Task {name} done

#スクリプトが直接実行された場合に、main関数を非同期に実行
if __name__ == '__main__':
    #asyncio.run()は、非同期関数を実行し、完了するまでプログラムの実行を続ける
    asyncio.run(main())