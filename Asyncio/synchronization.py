import asyncio

#A shared variable i.e may be database, file or any resources
shared_resource = 1


# An asyncio lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        #Critical section starts
        print(f"Resource before modification : {shared_resource}")

        shared_resource +=1# Modify the shared resources
        await asyncio.sleep(1) # Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        #The critical section starts when the program acquires the lock, and it ends when the program releases the lock, ensuring that only one coroutine can execute the protected code at a time."
async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

asyncio.run(main())