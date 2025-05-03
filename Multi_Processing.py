from multiprocessing import Process
import os
import time


def square_num():
    for i in range(100):
        i*i
        time.sleep(0.1)


processes =[]
num_processes = os.cpu_count() # number of cpu in machine


# create processes
for i in range (num_processes):
    p = Process(target = square_num )
    processes.append(p)

#start
for p in processes:
    p.start()
#join
for p in processes:
    p.join()

print('end main')


from multiprocessing import Process
import pandas as pd

def preprocess_data(chunk):
    # Example: Square a column in the chunk
    chunk['squared'] = chunk['value'] ** 2
    print(chunk)

if __name__ == "__main__":
    # Simulate a large dataset
    data = pd.DataFrame({'value': range(100)})
    
    # Split data into chunks
    chunks = [data.iloc[i:i+25] for i in range(0, len(data), 25)]
    
    processes = []
    
    # Create a process for each chunk
    for chunk in chunks:
        p = Process(target=preprocess_data, args=(chunk,))
        processes.append(p)
    
    # Start and join processes
    for p in processes:
        p.start()
    for p in processes:
        p.join()