import random
def StressTest(N, M):
    while True:
        n = random.randint(2, N)
        a = [random.randint(0, M) for _ in range(n)]
        print(a)

        result1 = MaxPairwiseProductNaive(a)
        result2 = MaxPairwiseProductFast(a)

        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer: ", result1, result2)
            break


StressTest(10, 100000)
StressTest(N=5, M=9)
StressTest(N=1000, M=200000)


