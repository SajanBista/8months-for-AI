import asyncio
import random

async def download_file(file_number):
    print(f"Start downloading file {file_number}")
    download_time = random.randint(1, 5)
    await asyncio.sleep(download_time)
    print(f"Finished downloading file {file_number} in {download_time} seconds")
    return f"file_{file_number}.txt"

async def main():
    tasks = []
    for i in range(1, 6):  # simulate downloading 5 files
        tasks.append(download_file(i))
    
    # Run all tasks concurrently
    results = await asyncio.gather(*tasks)
    
    print("\nAll files downloaded:")
    for result in results:
        print(result)

# Run the main coroutine
asyncio.run(main())
