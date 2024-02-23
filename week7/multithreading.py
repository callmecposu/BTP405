from threading import Thread
import time

def task():
    for i in range(10000):
        num = i**i

if __name__ == '__main__':
    threads = []
    start = time.time()
    for i in range(5):
        t = Thread(target=task)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f'Elapsed with multithreading: {end - start}s')