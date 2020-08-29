n = int(input())
fib_list = []
fib_list.insert(0, 0)
fib_list.insert(1, 1)
for i in range(2, n+1):
    fib_list.append((fib_list[i-1] + fib_list[i-2])%10)

print(fib_list[n])