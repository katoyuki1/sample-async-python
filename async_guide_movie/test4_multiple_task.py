'''
asyncioライブラリを使って、複数の数値の平方を非同期に計算するシンプルなプログラム
'''
import asyncio

#この関数は、与えられた数値の平方を計算します。async defは、この関数が非同期であることを示します。
async def compute_square(number):
    #asyncio.sleep(1)により、非同期に1秒間処理を一時停止します。これは、たとえば外部APIからの応答を待つなど、実際のアプリケーションでの遅延をシミュレートするために使われます。
    await asyncio.sleep(1)
    #計算した平方を出力します。f"{}"は、文字列内に変数の値を埋め込むためのフォーマット文字列（f-string）です。
    print(f"Square of {number} is {number * number}")
    return number * number

async def main():
    #平方を計算する数値のリストを定義
    numbers = [1, 2, 3, 4, 5]
    #リスト内包表記を使って、各数値に対してcompute_square関数を非同期タスクとして実行するためのタスクリストを作成します。
    #asyncio.create_task()は、非同期関数を非同期タスクとしてスケジュールし、実行を開始します。
    tasks = [asyncio.create_task(compute_square(number)) for number in numbers]
    print(f"tasksの型は{type(tasks)}") # list型

    #作成したすべての非同期タスクが完了するのを待ちます。
    #awaitを使うことで、これらのタスクの結果（この場合は各数値の平方）を収集し、squares変数に格納します。
    #*tasksは、リストの要素を個別の引数としてgatherに渡すための構文です。
    squares = await  asyncio.gather(*tasks)
    print(f"Squares: {squares}")


asyncio.run(main())