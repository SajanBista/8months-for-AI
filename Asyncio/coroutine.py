import asyncio



# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay)
    print("Data fetched")
    return {"data":"Some data"}

#coroutine function
async def main():
    print("start of main coroutine")
    #await #only used inside async function
    task = fetch_data(2)
    # await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await task
    print(f"Received result: {result}")
    print("End of main coroutine")

#run the main coroutine
asyncio.run(main())