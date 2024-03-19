import time
import functools



@functools.lru_cache()
def Fuctorial(n):
    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Fuctorial(n-1)

start = time.time()
for i in range(1,11):
    print('{}! = {}'.format(i, Fuctorial(i)))
    
end = time.time()
print('Czas wykonania: {} sekund'.format(end-start))

print(Fuctorial.cache_info())



