import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(3) # ３秒待ってから、次の処理へ
    print('... World!')

asyncio.run(main())