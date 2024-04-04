# pip install pytest
# pip install pytest-asyncio

import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    print({"data":123})
    return {"data":123}

async def main():
    await fetch_data()

asyncio.run(main())