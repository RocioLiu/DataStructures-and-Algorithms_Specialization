## Fractional_knapsack

# Task: The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
#
# Input Format: The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
#   The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣 𝑖 and 𝑤 𝑖 —the
#   value and the weight of 𝑖-th item, respectively.
#
# Constraints: 1 ≤ 𝑛 ≤ 10**3 , 0 ≤ 𝑊 ≤ 2 * 10**6 ; 0 ≤ 𝑣 𝑖 ≤ 2 * 10**6 , 0 < 𝑤 𝑖 ≤ 2 * 10**6 for all 1 ≤ 𝑖 ≤ 𝑛.
#   All the numbers are integers.
#
# Output Format: Output the maximal value of fractions of items that fit into the knapsack. The absolute value
#   of the difference between the answer of your program and the optimal value should be at most 10**−3 .
#   To ensure this, output your answer with at least four digits after the decimal point (otherwise your answer,
#   while being computed correctly, can turn out to be wrong because of rounding issues).
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    unit_value = []
    for i in range(len(weights)):
        unit_value.append(values[i]/weights[i])

    #unit_value = sorted(unit_value, reverse=True)
    unit_value_sort_idx = [i[0] for i in sorted(enumerate(unit_value), key=lambda x:x[1], reverse=True)]
    for i in range(len(weights)):
        item_num = unit_value_sort_idx[i]
        capacity -= weights[item_num]
        if capacity >= 0:
            value += values[item_num]
        else:
            value += unit_value[item_num]*(weights[item_num]+capacity)
            break

    return value




if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[:2]
    values = data[2:(2 * n + 1):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

