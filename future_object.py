import asyncio
import random


async def waiter(future):
    await future
    print(f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу")


async def setter(future):
    await asyncio.sleep(random.uniform(1, 3))
    future.set_result(True)


async def main():
    future = asyncio.Future()
    task1 = asyncio.create_task(waiter(future))
    task2 = asyncio.create_task(setter(future))
    await asyncio.gather(task1, task2)


asyncio.run(main())
