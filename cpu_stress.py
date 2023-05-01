import time

start = time.time()
i = 2**10
t = 1

for n in range(1, int(i)):
    t+=n
    print(n, t)

end = time.time()
print(end-start, "ms")