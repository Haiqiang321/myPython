# _*_ coding:utf-8 _*_

# @Author :Haiqiang
# @Time :2023/12/18 11:23
# @FileName :daemon.py

import asyncio


async def func1():
    print("你好，小一")
    await asyncio.sleep(2)
    print("你好，小一")


async def func2():
    print("你好，小二")
    await asyncio.sleep(2)
    print("你好，小二")


async def func3():
    print("你好，小三")
    await asyncio.sleep(2)
    print("你好，小三")


async def main():
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()



