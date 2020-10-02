
# Naive method
def lcm_naive(a, b):
    for i in range(1, a*b + 1):
        if i % a == 0 and i % b == 0:
            return i


# Faster method
def euclidGCD(a, b):
    if b == 0:
        return a
    else:
        a_prime = a % b
        return euclidGCD(b, a_prime)


def lcm_fast(a, b):
    c = euclidGCD(a, b)
    return int(a * b / c)

a, b = map(int, input().split())

print(lcm_fast(a, b))