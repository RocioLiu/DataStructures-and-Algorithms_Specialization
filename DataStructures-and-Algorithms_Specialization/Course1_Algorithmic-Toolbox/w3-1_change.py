## Money Change

# Task: The goal in this problem is to find the minimum number of coins needed to change
# the input value (an integer) into coins with denominations 1, 5, and 10.
#
# Input Format: The input consists of a single integer 𝑚. Constraints. 1 ≤ 𝑚 ≤ 10**3 .
#
# Output Format: Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.

def change_naive(m):
    count = 0
    leftover = m
    for i in (10, 5):
        count += int(leftover/i)
        leftover %= i
    count += int(leftover)

    return count

m = int(input())

print(change_naive(m))


