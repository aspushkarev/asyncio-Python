import asyncio

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

counts = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}


async def counter(name, delay) -> None:
    while counts[name] < max_counts[name]:
        await asyncio.sleep(delay)
        counts[name] += 1
        print(f"{name}: {counts[name]}")


async def main() -> None:
    tasks = [asyncio.create_task(counter(i, delays[i])) for i in counts]
    await asyncio.gather(*tasks)


asyncio.run(main())