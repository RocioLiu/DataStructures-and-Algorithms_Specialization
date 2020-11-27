import sys

# distance = d
# tank = m


def compute_min_refills(distance, tank, stops):
    stops.append(distance)  # last stop
    current_remain = tank - stops[0]
    count = 0
    for i in range(1, len(stops)):
        delta = stops[i] - stops[i - 1]
        if delta > current_remain:
            current_remain = tank
            count += 1
        current_remain -= delta
        if current_remain < 0: break

    if current_remain < 0:
        count = -1
    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))



for i in range(len(head)-1,0, -1):
    print(head[i])