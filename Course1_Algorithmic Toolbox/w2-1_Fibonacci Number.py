import time

def fibonacci_naive(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_fast(n):
    fib_list = []
    fib_list.insert(0, 0)
    fib_list.insert(1, 1)
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list[n]



n = int(input())

start_time = time.time()
fibonacci_naive(n=10)
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
fibonacci_fast(n=10)
print("--- %s seconds ---" % (time.time() - start_time))



## The format to submit as the assignment
n = int(input())
fib_list = []
fib_list.insert(0, 0)
fib_list.insert(1, 1)
for i in range(2, n+1):
    fib_list.append(fib_list[i-1] + fib_list[i-2])

print(fib_list[n])

