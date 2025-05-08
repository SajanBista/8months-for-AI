import asyncio

async def access_resource(semaphore, resource_id):
    async with semaphore:
        #Simulate accessing a limited resources
        print(f"Accessing resources { resource_id}")
        await asyncio.sleep(1) # Simulate work 
        print(f"Releasing resource {resource_id}")
async def main():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range (5)))

asyncio.run(main())

