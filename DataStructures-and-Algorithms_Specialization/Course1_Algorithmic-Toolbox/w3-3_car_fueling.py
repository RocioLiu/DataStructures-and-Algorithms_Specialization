import sys

# distance = d
# tank = m


def compute_min_refills(distance, tank, stops):
    if tank > distance:
        return 0
    if distance - stops[-1] > tank:
        return -1
    stopsx = stops.copy()
    refill_candidate = []
    refill_here = [0]
    refill_here_idx = 0
    while len(stopsx) > 0:
        refill_candidate = [(idx, stop) for (idx, stop) in enumerate(stopsx) if stop - refill_here[-1] <= tank]
        if len(refill_candidate) > 0:
            refill_here.append(refill_candidate[-1][1])
            refill_here_idx = refill_candidate[-1][0]
            stopsx = stopsx[refill_here_idx + 1:]
            if refill_here[-1] + tank > distance:
                break
        else:
            return -1

    return len(refill_here) - 1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))



# 700
# 200
# 4
# 100 200 300 400

# 750
# 400
# 3
# 200 375 550


