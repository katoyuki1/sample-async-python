import asyncio

async def download_file(file_name):
    print(f"starting download {file_name}")
    await  asyncio.sleep(2)
    print(f"Finished downloading {file_name}")
    return f"{file_name} downloaded"

async def main():
    files_lst = ["file1.txt", "file2.txt", "file3.txt"]
    #ファイルリストの各ファイルに対してdownload_fileコルーチンを作成し、リストにまとめます。
    #修正前：download_coroutines = [download_file(file) for file in files_lst]　python3.11以降は
    download_tasks = [asyncio.create_task(download_file(file)) for file in files_lst]

    #asyncio.waitを使用して、すべてのダウンロードコルーチンが完了するのを非同期に待ちます。
    #return_when=asyncio.ALL_COMPLETEDは、すべてのコルーチンが完了するまで待つことを意味します。
    completed, pending = await asyncio.wait(download_tasks, return_when=asyncio.ALL_COMPLETED)

    #完了したダウンロードタスクのリストをループ処理します
    for download_task in completed:
        print(download_task.result())

asyncio.run(main())