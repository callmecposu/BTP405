import time

def task():
    for i in range(10000):
        num = i**i

start = time.time()

for i in range(5):
    task()

end = time.time()

print(f'Elapsed synchronously: {end - start}s')