n = int(input())
a = [int(x) for x in input().split()]

product = 0
for i in range(n):
    for j in range(i+1, n):
        product = max(product, a[i]*a[j])

print(product)


# Pack it as a function to be called in StressTest.py
def MaxPairwiseProductNaive(a):
    product = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            product = max(product, a[i] * a[j])

    return product

