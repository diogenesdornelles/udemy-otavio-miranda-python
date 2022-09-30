import asyncio
import time

"""
In async we run ONE BLOCK of code at a time but we cycle which block of code is running. Your program needs to be built 
around async though you can call normal (synchronous) functions from async program.
A - Add async keyword in front of your function declarations to make them awaitable.
B - Add await keyword when you call your async functions (without it they won’t run).
C - Create tasks from the async functions you wish to start asynchronously. Also wait for their finish.
D - Call asyncio.run to start the asynchronous section of your program.
"""


# Making awaitable by kw async
async def do_first():
    print("Running do_first block 1")
    for i in range(10):
        time.sleep(0.25)
        print(i)

    # Release execution.
    await asyncio.sleep(0)

    print("Running do_first block 3")
    for i in range(10):
        time.sleep(0.25)
        print(i)


async def do_second():
    print("Running do_second block 1")
    for i in range(10):
        time.sleep(0.25)
        print(i)

    # Release execution

    await asyncio.sleep(0)

    print("Running do_second block 2")
    for i in range(10):
        time.sleep(0.25)
        print(i)


async def do_greetings():
    print('Hello world do_greetings block 1')
    await asyncio.sleep(0)
    print('Hello world do_greetings block 2')


async def main():
    # Create tasks from the async functions
    task_1 = asyncio.create_task(do_first())
    task_2 = asyncio.create_task(do_second())
    task_3 = asyncio.create_task(do_greetings())
    # Also wait for their finish.
    await asyncio.wait([task_1, task_2, task_3])


if __name__ == "__main__":
    # Call asyncio.run to start the asynchronous section
    asyncio.run(main())
    asyncio.wait
