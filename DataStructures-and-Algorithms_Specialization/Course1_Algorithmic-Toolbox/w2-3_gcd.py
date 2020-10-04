## Greatest Common Divisor

# Task: Given two integers 𝑎 and 𝑏, find their greatest common divisor.

# Input Format: The two integers 𝑎, 𝑏 are given in the same line separated by space.

# Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 * 10**9

# Output Format: Output GCD(𝑎, 𝑏)

a, b = list(map(int, input().split()))

def euclidGCD(a, b):
    if b == 0:
        return a
    else:
        a_prime = a % b
        return euclidGCD(b, a_prime)


print(euclidGCD(b, a))


# start_time = time.time()
# euclidGCD(28851538, 1183019)
# print("--- %s seconds ---" % (time.time() - start_time))



# if b == 0:
#     best_d  = a
# else:
#     a_prime = a % b
#     best_d = 0
#     for d in range(1, a_prime + b):
#         if a_prime % d == 0 and b % d == 0:
#             best_d = d
#
# print(best_d)