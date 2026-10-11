import time

def slow(n):
    time.sleep(1)
    return n

menu = (slow(n) for n in range(3))
print(menu)
print(list(menu))
print(list(menu))