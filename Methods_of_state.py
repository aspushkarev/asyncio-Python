import asyncio

async def set_future_result(value, delay, future):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    future.set_result(value)
    print(f'Результат установлен.')
    return value

async def create_and_use_future():
    future = asyncio.Future()
    task = asyncio.create_task(set_future_result('Успех', 2, future))
    if future.done():
        print("Состояние Task до выполнения: Завершено")
    else:
        print("Состояние Task до выполнения: Ожидание")
    print("Задача запущена, ожидаем завершения...")

    await asyncio.gather(task)
    result = task.result()

    if future.done():
        print("Состояние Task после выполнения: Завершено")
    else:
        print("Состояние Task после выполнения: Ожидание")

    return result

async def main():

    result = await create_and_use_future()
    print("Результат из Task:", result)

asyncio.run(main())
