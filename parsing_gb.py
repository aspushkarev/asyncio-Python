# https://gbcdn.mrgcdn.ru/uploads/record/263242/attachment/e8689f8d35b106a0f553b33860cc9e28.mp4
#
# f = open(r'file.mp4', "wb")
#  ufr = s.get(url)
#  f.write(ufr.content)
#  f.close()

#
# import asyncio
#
# max_counts = {
#     "Counter 1": 13,
#     "Counter 2": 7
# }
#
# counters = {
#     "Counter 1": 0,
#     "Counter 2": 0
# }
#
#
# async def counter(name, relay) -> None:
#     maximum = max_counts.get(name)
#     for i in range(maximum):
#         digital = counters.get(name)
#         if digital < maximum:
#             digital += 1
#             counters.update({name: digital})
#             print(f"{name}: {digital}")
#             await asyncio.sleep(relay)
#
#
# async def main():
#     relay = 1
#     a, b = counters.keys()
#     tasks = [asyncio.create_task(counter(a, relay)), asyncio.create_task(counter(b, relay))]
#     await asyncio.gather(*tasks)
#
#
# asyncio.run(main())

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
    tasks = [asyncio.create_task(counter(i, delays[i]) for i in counts)]
    await asyncio.gather(*tasks)


asyncio.run(main())
