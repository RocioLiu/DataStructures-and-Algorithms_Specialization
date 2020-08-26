n = int(input())
a = [int(x) for x in input().split()]


index1 = 0
for i in range(1, len(a)):
    if a[i] > a[index1]:
        index1 = i

if index1 == 0:
    index2 = 1
else:
    index2 = 0

for i in range(1, len(a)):
    if i != index1 and a[i] > a[index2]:
        index2 = i

print(a[index1] * a[index2])


# Pack it as a function to be called in StressTest.py
def MaxPairwiseProductFast(a):
    index1 = 0
    for i in range(1, len(a)):
        if a[i] > a[index1]:
            index1 = i

    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for i in range(1, len(a)):
        if i != index1 and a[i] > a[index2]:
            index2 = i

    print('index1 and index2: ', index1, index2)
    return a[index1] * a[index2]



