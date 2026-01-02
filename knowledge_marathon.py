import asyncio


async def study_course(student, course, steps, speed):
    print(f"{student} начал проходить курс {course}.")
    reading_time = steps / speed
    await asyncio.sleep(reading_time)
    print(f"{student} прошел курс {course} за {round(reading_time, 2)} ч.")


async def main():
    students = {
        'Алекс': {"course": "Асинхронный Python", "steps": 515, "speed": 78},
        'Мария': {"course": "Многопоточный Python", "steps": 431, "speed": 62},
        'Иван': {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
    }
    tasks = [asyncio.create_task(study_course(key, value["course"], value["steps"], value["speed"])) \
             for key, value in students.items()]
    await asyncio.gather(*tasks)


asyncio.run(main())
