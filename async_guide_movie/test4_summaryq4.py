'''
0〜999の間の平方（２乗）の和を非同期で計算し、その結果を出力
'''
import asyncio

async def compute():
    return sum(i * i for i in range(1000))
 
async def main():
    result = await compute()
    print(result)


asyncio.run(main())