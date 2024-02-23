from multiprocessing import Process
import time

def task():
    for i in range(10000):
        num = i**i

if __name__ == '__main__':
    processes = []
    start = time.time()
    for i in range(5):
        p = Process(target=task)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print(f'Elapsed with multiprocessing: {end - start}s')