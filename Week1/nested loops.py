import time

start_time = time.time()
var = 1000

for i in range(var):
    for j in range(var):
        print(0, end= " ")
    print()

print(round((time.time() - start_time), 4))