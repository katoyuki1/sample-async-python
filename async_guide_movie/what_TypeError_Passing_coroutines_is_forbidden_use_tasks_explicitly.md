「test_multiple.py」で以下エラーが発生  
'''
  File "/Users/y-kato/.pyenv/versions/3.11.4/lib/python3.11/asyncio/tasks.py", line 415, in wait
    raise TypeError("Passing coroutines is forbidden, use tasks explicitly.")
TypeError: Passing coroutines is forbidden, use tasks explicitly.
sys:1: RuntimeWarning: coroutine 'download_file' was never awaited
'''

このエラーメッセージは、非同期プログラミングを行っているPythonのコードで問題が発生したことを示しています。  
具体的には、asyncio.wait関数を使用する際にコルーチンを直接渡そうとしたため、TypeErrorが発生しています。  
さらに、あるコルーチンがawaitされずに終了したことを示すRuntimeWarningも表示されています。これらの問題について一つずつ解説します。  

# TypeError: Passing coroutines is forbidden, use tasks explicitly.
このエラーは、asyncio.wait関数にコルーチンのリストを直接渡したことが原因で発生しています。  
asyncio.waitはタスク（asyncio.Taskオブジェクト）のセットを引数として期待していますが、ここではコルーチンが直接渡されています。  
Python 3.11からは、asyncio.waitにコルーチンを直接渡すことが禁止され、明示的にタスクを使用する必要があります。  

これを修正するには、コルーチンをasyncio.create_task関数でタスクに変換し、それらのタスクをasyncio.waitに渡す必要があります。  
具体的には、以下のように修正します。  

修正前:  
`
download_coroutines = [download_file(file) for file in files_lst]  
completed, pending = await asyncio.wait(download_coroutines, return_when=asyncio.ALL_COMPLETED)  
`

修正後:  
`
download_tasks = [asyncio.create_task(download_file(file)) for file in files_lst]  
completed, pending = await asyncio.wait(download_tasks, return_when=asyncio.ALL_COMPLETED)  
`

# RuntimeWarning: coroutine 'download_file' was never awaited
この警告は、download_fileコルーチンが実行（await）されずにプログラムが終了したことを示しています。  
この場合、download_fileコルーチンがasyncio.create_taskを使ってタスクに変換され、asyncio.waitでawaitされるべきですが、適切にawaitされていないことが原因で警告が出ています。  
上記の修正を行うことで、この警告も解消されるはずです。  

これらの修正により、複数のファイルダウンロードを非同期に実行するコードが正しく動作し、TypeErrorもRuntimeWarningも解消されます。  
非同期IOにおけるタスクの使用は、非同期プログラミングにおける基本的なパターンの一つですので、これを機に理解を深めると良いでしょう。  