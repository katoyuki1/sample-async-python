'''
@pytest.mark.asyncioデコレータを使用して、次に定義されるテスト関数が非同期であることをpytestに示します。
これにより、pytestはこのテストを非同期I/Oイベントループ内で実行します。
このデコレータはpytest-asyncioプラグインによって提供されます。
'''
import pytest
from test6_async_app import fetch_data

@pytest.mark.asyncio
async def test_fetch_data():
    #await式を使用して、fetch_data関数からの結果を非同期に待ちます。この関数が完了すると、その戻り値がresultに代入されます
    result = await fetch_data()
    #assertステートメントを使用して、fetch_data関数から返された結果が期待通りであるかを確認します。
    #期待される結果は辞書{"data": 123}で、これが実際のresultと一致することを確認しています。
    #一致しない場合、"Expected result did not match!"というメッセージと共にアサーションエラーが発生します。
    assert result == {"data": 123}, "Expected result did not match!"

@pytest.mark.asyncio
async def test_unmatch_fetch_data():
    result = await fetch_data()
    assert result != {"data": 1223}, "Expected result did not match!"