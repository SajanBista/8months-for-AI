from threading import Thread
import os
import time

def squared_num():
    for i in range(100):
        i*i
        time.sleep(0.1)

if __name__ == "__main__":
    threads = []
    num_threads = 20
    for i in range(num_threads):
        t = Thread(target = squared_num)
        threads.append(t)

    #Start
    for T in threads:
        t.start()
    for T in threads:
        t.join()

    print('End Main')

