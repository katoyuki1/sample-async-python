import asyncio
import time
import logging

#ロギングの基本設定。ログレベルをDEBUGに設定し、ログのフォーマットにはタイムスタンプ、ログレベル、メッセージを含めるよう指定。
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s:%(message)s")

#タスクの名前（name）と、そのタスクが"実行"されるべき持続時間（duration）を引数
async def simulate_io_task(name, duration):
    logging.info(f"Task {name}: Starting with duration of {duration}") #タスクの開始をログに記録
    await asyncio.sleep(duration) #I/O操作をシミュレートするための代用
    logging.info(f"Task {name}: Completed") #タスクの完了をログに記録
    return duration #タスクが"実行"された持続時間を返す


async def main():
    start_time = time.perf_counter() #タスク実行の開始時間を記録
    tasks = [simulate_io_task(f"Task{i}", i) for i in range(1, 4)] #1秒から3秒の持続時間で3つの非同期I/Oタスクを生成し、それらをリストに格納
    durations = await asyncio.gather(*tasks) #すべての非同期タスクを同時に実行し、それぞれのタスクから返される持続時間をリストdurationsに格納
    total_duration = sum(durations) #すべてのタスクの持続時間の合計を計算
    end_time = time.perf_counter() #タスク実行の終了時間を記録

    #すべてのタスクが完了するのにかかった実際の時間と、タスクが"実行"された合計持続時間をログに記録
    logging.info(
        f"All tasks completed in {end_time - start_time} seconds, total sleep duration was {total_duration} seconds")

asyncio.run(main())