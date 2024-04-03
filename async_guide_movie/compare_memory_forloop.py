import sys

# Forループを使用してリストを生成
squares_for_loop = []
for i in range(1000):
    squares_for_loop.append(i * i)
print(f"for loop list size: {sys.getsizeof(squares_for_loop)} bytes")

# ジェネレータ式
squares_generator = (i * i for i in range(1000))
print(f"Generator expression size: {sys.getsizeof(squares_generator)} bytes")

# リスト内包表記
squares_list_comprehension = [i * i for i in range(1000)]
print(f"List comprehension size: {sys.getsizeof(squares_list_comprehension)} bytes")

'''
【メモ】
sys.getsizeof()関数は、引数として渡されたオブジェクトのメモリサイズをバイト単位で返す。
ジェネレータ式が最もメモリ効率が良いことが期待されるが、その代わりに一度に一つの結果しかアクセスできないことに注意する。

一方、forループとリスト内包表記はリスト全体をメモリに格納するため、大きなデータを扱う場合はより多くのメモリを消費する
'''