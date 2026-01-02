import asyncio


async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    # Создаем задачи для асинхронного выполнения
    student_dict = {'Алекс': 5, 'Мария': 3, 'Иван': 4}
    tasks = [read_book(key, value) for key, value in student_dict.items()]
    await asyncio.gather(*tasks)

asyncio.run(main())
