# single_threaded.py
import time

COUNT = 50_000_000


def countdown(n):
    while n > 0:
        n -= 1


start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)
